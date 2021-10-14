#!/usr/bin/tclsh
set lsnPort [expr [expr ($argc >= 1)] ? {[lindex $argv 0]} : 9700]
proc Accept {newSock addr port} {
    puts "\nAccepted $newSock from $addr port $port @ [clock format [clock seconds] -format {%Y.%m.%d_%H:%M:%S}]\n"
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
            puts "Response msg via $sock:\n$resMsg"
            puts -nonewline $sock $resMsg
            if [catch {flush $sock} err] {
                puts "Resonse msg failed: $err"
            }
        }
    } else {
        close $sock
    }
}
proc ProcessMsg {sockID recdMsg} {
    set responseMsg "HTTP/1.1 200 OK\r\n"
    append responseMsg "Content-Length: 0\r\n\r\n"
    return $responseMsg
}
set listenSocket [socket -server Accept $lsnPort]
fconfigure $listenSocket -translation lf
vwait forever
