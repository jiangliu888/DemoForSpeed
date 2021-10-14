#!/usr/bin/tclsh
#package req Thread
package req tdom
package req math

# Configurations
# the listener port
set lsnPort 9999
# timeout for receiving data (seconds)
set dataTO 300
# transfer package length
set pkgLen 1024
# object storage dir
set storageDir "[pwd]/store"
if {![file exists $storageDir]} {
   file mkdir $storageDir
}
# oss hostname
set ossHostname "oss-aiwan-cn-beijing.aliyuncs.com"
# specify the log dir and file
set logDir "log"
set logFile "[clock format [clock seconds] -format {%Y.%m.%d_%H.%M.%S}].log"
# Open log file
if {![file exists $logDir]} {
   file mkdir $logDir
}
set logFileId [open "$logDir/$logFile" w]

proc ldelete { listName element } {
    upvar $listName list
    set ix [lsearch -exact $list $element]
    if {$ix >= 0} {
       set list [lreplace $list $ix $ix]
       return
    }
}

proc Log {args} {
    global logFileId
    puts "[clock format [clock seconds] -format "%x %X"]: [concat $args]\n"
    puts $logFileId "[clock format [clock seconds] -format "%x %X"]: [concat $args]\n"
    flush stdout
    flush $logFileId
}

set fileList ""
proc ListFiles {path} {
    global fileList
    set items [glob $path/*]
    foreach item $items {
        if {[file isdirectory $item]} {
            ListFiles $item
        } else {
            lappend fileList $item
        }
    }
}

#################################################################################
# Socket server
#################################################################################
proc Accept {newSock addr port} {
    Log "\nAccepted $newSock from $addr port $port @ [clock format [clock seconds] -format {%Y.%m.%d_%H:%M:%S}]\n"
    fconfigure $newSock -blocking 0
    fconfigure $newSock -encoding binary
    fconfigure $newSock -translation lf
    fileevent $newSock r [list readSocket $newSock]
}
proc readSocket {sock} {
    if {[catch {read $sock} gotMsg]} {
        if {[regexp {reset by peer} $gotMsg]} {
            close $sock
        } else {
            error $gotMsg
        }
        return
    }
    if {($gotMsg != "")} {
#        binary scan $gotMsg "H[expr ([string length $gotMsg] * 2)]" acceptMsg
        # Decode and encode message
        set resMsg [ProcessMsg $sock gotMsg]
        if {$resMsg != ""} {
            Log "Response msg via $sock:\n$resMsg"
            puts -nonewline $sock $resMsg
            if [catch {flush $sock} err] {
                Log "Resonse msg failed: $err"
            }
        }
    } else {
        close $sock
    }
}

#################################################################################
# Description: Process the received message.
# Input: recdMsg, the received messgae (in Hex)
#
# Output: responseMsg, the message to be sent (in Hex)
#
# Histry:
# 2019/09/19 Betty created
#################################################################################
proc ProcessMsg {sockID recdMsg} {
    global storageDir lReserveAID dataTO pkgLen ossHostname fileList
    upvar $recdMsg recMsg
    # check the \r\n\r\n
    if {![regexp {(.*)\r\n\r\n(.*)} $recMsg match reqHeader reqBody]} {
        Log "Bad Request: \r\n\r\n not found."
        Log "[string length $recMsg]"
    }
    # this is for the 100 continue feature
    if {[regexp {Expect: 100-continue} $reqHeader]} {
        Log "Expect: 100-continue"
        puts -nonewline $sockID "HTTP/1.1 100 Continue"
        if [catch {flush $sockID} err] {Log "Error: flush to $sockID failed: $err."; return}
    }
    set lReqBody [string length $reqBody]
    regsub "%2F" $reqHeader "/" reqHeader
    Log "\n$sockID got msg header: $reqHeader\n"
    # Decode
    set method [lindex $reqHeader 0]
    set request [lindex $reqHeader 1]
    if {![regexp {(.*)\?(.*)} [lindex $reqHeader 1] match request reqParameters]} {
        Log "No parameters found."
    }
    # check the host name
    if {![regexp {Host: (.*?)\r\n} $reqHeader match host]} {
        Log "No host found."
        set responseMsg "HTTP/1.1 400 Bad Request\r\n"
        append responseMsg "Content-Length: 0\r\n\r\n"
        return $responseMsg
    }
    if [regexp "(.+)\.$ossHostname" $host match bucketName] {
        set filePath "$storageDir/[set bucketName][set request]"
    } else {
        set filePath $storageDir$request
    }
    Log "======$method===$request=====$filePath===="
    regsub -all {%2F} $request {/} request
    regsub -all {%2F} $filePath {/} filePath
    Log "==========after regsub: ======$method===$request=====$filePath===="
    # methods
    switch -glob -- $method {
        {HEAD} {
            if {![file exists $filePath]} {
                Log "Object $filePath not found."
                set responseMsg "HTTP/1.1 404 NOT FOUND\r\n"
                append responseMsg "Content-Length: 0\r\n\r\n"
            } else {
                Log "Found object $filePath."
                set responseMsg "HTTP/1.1 200 OK\r\n"
                append responseMsg "x-oss-object-type: Normal\r\n"
                append responseMsg "Last-Modified: [clock format [file mtime $filePath] -format {%a, %d %b %Y %H:%M:%S GMT}]\r\n"
                append responseMsg "Etage: [GenReqID 32]\r\n"
                append responseMsg "Content-Length: [file size $filePath]\r\n"
            }
            append responseMsg "x-oss-request-id: [GenReqID]\r\n"
            append responseMsg "Date: [clock format [clock seconds] -format {%a, %d %b %Y %H:%M:%S GMT}]\r\n"
            append responseMsg \r\n
            return $responseMsg
        }
        {PUT} {
            if {![regexp {Content-Length: ([\d]+)} $reqHeader match cLen]} {
                set cLen 0
                Log "No Content-Length found for PUT request, regarded as PUT Bucket."
                if {[catch {file mkdir $filePath$bucketName} err]} {
                    Log "Mkdir $filePath$bucketName failed: $err."
                    set responseMsg "HTTP/1.1 400 TooManyBuckets\r\n"
                    append responseMsg "Content-Length: 0\r\n\r\n"
                    return $responseMsg
                }
                set responseMsg "HTTP/1.1 200 OK\r\n"
                append responseMsg "Content-Length: 0\r\n\r\n"
                return $responseMsg
            }
            # open the object file
            if [info exists bucketName] {
                Log "Found the bucket name: $bucketName"
                set fid [open $filePath w]
                fconfigure $fid -encoding binary
                fconfigure $fid -translation lf
                puts -nonewline $fid $reqBody
                flush $fid
                if { $lReqBody < $cLen} {
                    for {set i 0} {$i < [expr $dataTO * 100] && $lReqBody < $cLen} {incr i} {
                        after 10
                        set reqBody [read $sockID]
                        puts -nonewline $fid $reqBody
                        flush $fid
                        incr lReqBody [string length $reqBody]
                    }
                    Log "lReqBody is $lReqBody; i is $i; cLen is $cLen"
                }
                close $fid
                if {$lReqBody > $cLen} {
                    Log "Bad Request: Data is larger than the Content-length: [string length $reqBody] > $cLen"
                    set responseMsg "HTTP/1.1 400 Bad Request\r\n"
                    append responseMsg "Content-Length: 0\r\n\r\n"
                    return $responseMsg
                }
                if {$lReqBody < $cLen} {
                    Log "The data still not completed. Timeout: $lReqBody < $cLen"
                    set responseMsg "HTTP/1.1 400 Timeout\r\n"
                    append responseMsg "Content-Length: 0\r\n\r\n"
                    return $responseMsg
                }
                set responseMsg "HTTP/1.1 200 OK\r\n"
                append responseMsg "Content-Length: 0\r\n\r\n"
                return $responseMsg
            } else {
                Log "Unknown request as the content length is $cLen with no bucket name specified."
                set responseMsg "HTTP/1.1 400 Timeout\r\n"
                append responseMsg "Content-Length: 0\r\n\r\n"
                return $responseMsg
            }
        }
        {GET} {
            switch -regexp -- $request {
                {/.+} {
                    # get content
                    if {![file exists $filePath]} {
                        Log "Object $filePath not found."
                        set responseMsg "HTTP/1.1 404 NOT FOUND\r\n"
                        append responseMsg "Content-Length: 0\r\n\r\n"
                        append responseMsg \r\n
                        return $responseMsg
                    }
                    set fileSize [file size $filePath]
                    if {[catch {open $filePath r} fid]} {
                        Log "Open the object file $filePath failed!\n$fid"
                        set responseMsg "HTTP/1.1 400 Bad Request\r\n"
                        append responseMsg "Content-Length: 0\r\n\r\n"
                        return $responseMsg
                    }
                    fconfigure $fid -encoding binary
                    fconfigure $fid -translation lf
                    set rangeStart 0
                    set rangeEnd [expr $fileSize -1]
                    # send the response header for full file
                    set responseMsg "HTTP/1.1 200 OK\r\n"
                    append responseMsg "Server: AliyunOSS\r\n"
                    append responseMsg "x-oss-object-type: Normal\r\n"
                    append responseMsg "x-oss-request-id: [GenReqID]\r\n"
                    append responseMsg "Date: [clock format [clock seconds] -format {%a, %d %b %Y %H:%M:%S GMT}]\r\n"
                    append responseMsg "Content-Type: application/octet-stream\r\n"
                    append responseMsg "Last-Modified: [clock format [file mtime $filePath] -format {%a, %d %b %Y %H:%M:%S GMT}]\r\n"
                    append responseMsg "Etage: [GenReqID 32]\r\n"
                    append responseMsg "Content-Length: $fileSize\r\n"
                    append responseMsg "\r\n"
                    puts -nonewline $sockID $responseMsg
                    flush $sockID
                    # transfer file data
                    # readLength will save how many bytes have been read
                    set readLength 0
                    if {$rangeStart > 0} {
                        #incr readLength [expr ($rangeStart - 1)]
                        incr readLength $rangeStart
                        read $fid $readLength
                    }
                    while { ![eof $fid] && $readLength <= $rangeEnd} {
                        set leftLen [expr $rangeEnd - $readLength + 1]
                        set lenThisTime [expr {($leftLen <= $pkgLen) ? $leftLen : $pkgLen}]
                        set dataThisTime [read $fid $lenThisTime]
                        puts -nonewline $sockID $dataThisTime
                        flush $sockID
                        incr readLength $lenThisTime
                    }
                    close $fid
                    Log "Transfer file data done."
                    return ""
                }
                {/} {
                    if [info exists bucketName] {
                        # list all the objects under the bucket
                        set responseMsg "HTTP/1.1 200 OK\r\n"
                        append responseMsg "Date: [clock format [clock seconds] -format {%c %H.%M.%S}]\r\n"
                        append responseMsg "Content-Type: application/xml\r\n"
                        append responseMsg "Connection: keep-alive\r\n"
                        append responseMsg "Server: AliyunOSS\r\n"
                        append responseMsg "x-oss-request-id: [GenReqID]\r\n"
                        # form the xml
                        set body {<?xml version="1.0" encoding="UTF-8"?>
<ListBucketResult xmlns="http://doc.oss-cn-hangzhou.aliyuncs.com">
<Name>oss-example</Name>
<Prefix></Prefix>
<Marker></Marker>
<MaxKeys>100</MaxKeys>
<Delimiter></Delimiter>
<IsTruncated>false</IsTruncated>
                        }
                        set fileList ""
                        ListFiles $storageDir/$bucketName
                        foreach file $fileList {
                            regsub $storageDir/$bucketName $file "" name
                            append body "
    <Contents>
        <Key>[lindex [split $name /] end]</Key>
        <LastModified>[clock format [file mtime $file] -format "%Y-%m-%dT%H:%M:%S.000Z"]</LastModified>
        <ETag> [GenReqID 32]</ETag>
        <Type>Normal</Type>
        <Size>[file size $file]</Size>
        <StorageClass>Standard</StorageClass>
        <Owner>
            <ID>aiwan</ID>
            <DisplayName>[lindex [split $name /] end]</DisplayName>
        </Owner>
    </Contents>
                            "
                        }
                        append body {
</ListBucketResult>}
                        append responseMsg "Content-Length: [string length $body]\r\n\r\n"
                        append responseMsg $body
                        return $responseMsg
                    } else {
                        # list all the bucket
                        cd $storageDir
                        set lFolders [glob *]
                        set responseMsg "HTTP/1.1 200 OK\r\n"
                        append responseMsg "Date: [clock format [clock seconds] -format {%c %H.%M.%S}]\r\n"
                        append responseMsg "Content-Type: application/xml\r\n"
                        append responseMsg "Connection: keep-alive\r\n"
                        append responseMsg "Server: AliyunOSS\r\n"
                        append responseMsg "x-oss-request-id: [GenReqID]\r\n"
                        # form the xml
                        set body {<?xml version="1.0" encoding="UTF-8"?>
<ListAllMyBucketsResult>
  <Owner>
    <ID>55555</ID>
    <DisplayName>55555</DisplayName>
  </Owner>
  <Buckets>
                        }
                        foreach folder $lFolders {
                            if {[file isdirectory $folder]} {
                                append body {
        <Bucket>
          <CreationDate>2019-09-17T18:12:43.000Z</CreationDate>
          <ExtranetEndpoint>test</ExtranetEndpoint>
          <IntranetEndpoint>test</IntranetEndpoint>
          <Location>oss-cn-shanghai</Location>
            <Name>}
                                append body $folder
                                append body {</Name>
          <StorageClass>Standard</StorageClass>
        </Bucket>
                                }
                            }
                        }
                        append body {
  </Buckets>
</ListAllMyBucketsResult>}
                        cd ../
                        append responseMsg "Content-Length: [string length $body]\r\n\r\n"
                        append responseMsg $body
                        return $responseMsg
                    }
                }
                default {
                    Log "Unknown request: $request."
                    set responseMsg "HTTP/1.1 400 Bad Request\r\n"
                    append responseMsg "Content-Length: 0\r\n\r\n"
                    return $responseMsg
                }
            }
        }
        default {
            Log "Unknown request: $request."
            set responseMsg "HTTP/1.1 400 Bad Request\r\n"
            append responseMsg "Content-Length: 0\r\n\r\n"
            return $responseMsg
        }
    }
    # Response
    return "Not implemented\r\n"
}

proc RandomChar {} {
    set id [expr {rand()*36 + 55}]
    set id [expr int($id)]
    if {$id < 65} {
        incr id -7
    }
    return [binary format c $id]
}

proc GenReqID {{num 24}} {
    set id ""
    for {set i 0} {$i < $num} {incr i} {
        append id [RandomChar]
    }
    return $id
}

set listenSocket [socket -server Accept $lsnPort]
fconfigure $listenSocket -translation lf

Log "Started the oss simulator on port $lsnPort"
vwait forever
