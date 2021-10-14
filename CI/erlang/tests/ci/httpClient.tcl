#!/usr/bin/tclsh
if {$argc < 1} {
    puts "At least need the http server ip; the port is optional. Example: ./httpClient 10.193.0.2 9700"
    exit -1
}

set server [lindex $argv 0]
set delNum [expr [expr ($argc > 1)] ? {[lindex $argv 1]} : 40]
set port [expr [expr ($argc > 2)] ? {[lindex $argv 2]} : 9700]
set sid [socket $server $port]
set method GET
set payload ""
proc send {method payload} {
  global sid server
  puts -nonewline $sid "$method / HTTP/1.1\n"
  puts -nonewline $sid "Host: $server\n"
  puts -nonewline $sid "User-Agent: Mozilla/5.0 (Linux 4.15.0-46-generic) http/2.8.9 Tcl/8.6.5\n"
  puts -nonewline $sid "Connection: keepalive\n"
  puts -nonewline $sid "Accept: */*\n"
  puts -nonewline $sid "Accept-Encoding: gzip,deflate,compress\n"
  puts -nonewline $sid "Content-Type: application/x-www-form-urlencoded\n"
  puts -nonewline $sid "Content-Length: [string length $payload]\n"
  puts -nonewline $sid "\n"
  flush $sid
  set ret ""
  while {[gets $sid line] > 0} {
#puts "===============$line"
   if [regexp {(HTTP/\d\.\d \d{3}.*?)\n} $line match code] {set ret $code} else {continue}
  }
  return $ret
}
puts "running GET"
time {send GET ""} 20
puts "running PUT"
time {send PUT "abc"} 20
puts "running POST"
time {send POST "search"} 20
puts "running PATCH"
time {send PATCH "ttt"} 20
puts "running DELETE"
time {send DELETE "None"} $delNum