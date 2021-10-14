*** Settings ***
Resource          ../testcase/resource/SshKeyword.txt
Resource          ../testcase/resource/SaltKeyword.txt
Library           ../../libs/manager/ManagerKeyword.py
Library           ../../libs/prism/PrismKeyword.py
Library           DateTime

Suite Setup     Setup
Suite Teardown  close all connections

*** Variables ***
${capture_time}     ${10}
${default_time}     ${600}
${pkts_num}         ${200}
${default_pkts}     ${8000000}
${file_size}        ${307200}
${pcap_folder}      /dev/shm/

*** Test Cases ***
Get CPE Ports Info
    [Tags]  Series  SDWANDEV-2063
    switch connection   ${sess_salt_master}
    ${salt_res}=     Get CPE Ports   &{local_cpe}[minion_id]
    ${salt_ports}=  get lines matching regexp   ${salt_res}  [a-z0-9]*
    switch connection   ${sess_local_cpe}
    write   ifconfig | grep -v ^[[:space:]] | grep -v ^$| awk '{print $1}'
    ${ifconfig_res}=    read until prompt
    ${ifconfig_ports}=  get lines matching regexp   ${ifconfig_res}  [a-z0-9]*
    should be equal  ${salt_ports}    ${ifconfig_ports}

Tcpdump Capture on Series with Time Specified
    [Tags]    Series  SDWANDEV-2034    SDWANDEV-1984
    ${wait_to}=     evaluate  ${capture_time}+10
    switch connection   ${sess_salt_master_async}
    Start CPE Tcpdump Async    &{local_cpe}[minion_id]    &{local_cpe}[internet_if]   timeout=${capture_time}
    Start CPE Tcpdump Async    &{local_cpe}[minion_id]    &{local_cpe}[lan_if]   timeout=${capture_time}
    Start CPE Tcpdump Async    &{remote_cpe}[minion_id]    &{remote_cpe}[internet_if],&{remote_cpe}[lan_if]   timeout=${capture_time}
    switch connection   ${sess_salt_master}
    wait until keyword succeeds  ${wait_to}    500ms   Check Tcpdump Done    &{local_cpe}[minion_id]    &{local_cpe}[internet_if]
    wait until keyword succeeds  ${wait_to}    500ms   Check Tcpdump Done    &{local_cpe}[minion_id]    &{local_cpe}[lan_if]
    wait until keyword succeeds  ${wait_to}    500ms   Check Tcpdump Done    &{remote_cpe}[minion_id]    &{remote_cpe}[internet_if]
    wait until keyword succeeds  ${wait_to}    500ms   Check Tcpdump Done    &{remote_cpe}[minion_id]    &{remote_cpe}[lan_if]
    switch connection   ${sess_local_cpe}
    wait until keyword succeeds     2s  100ms   Check File Exists   /tmp/&{local_cpe}[internet_if].pcap
    Check Capture Time     local   /tmp/&{local_cpe}[internet_if].pcap  ${capture_time}     &{local_cpe}[passwd]
    switch connection   ${sess_remote_cpe}
    wait until keyword succeeds     2s  100ms   Check File Exists   /tmp/&{remote_cpe}[internet_if].pcap
    Check Capture Time     remote   /tmp/&{remote_cpe}[internet_if].pcap  ${capture_time}     &{remote_cpe}[passwd]

Tcpdump Capture on Series with Packets Specified
    [Tags]    Series  SDWANDEV-2035
    ${wait_to}=     evaluate  ${default_time}+10
    switch connection   ${sess_salt_master_async}
    Start CPE Tcpdump Async    &{local_cpe}[minion_id]    &{local_cpe}[internet_if]   ${default_time}   ${None}    -c ${pkts_num}
    Start CPE Tcpdump Async    &{remote_cpe}[minion_id]    &{remote_cpe}[internet_if]   ${default_time}   ${None}    -c ${pkts_num}
    switch connection   ${sess_salt_master}
    wait until keyword succeeds  ${wait_to}    500ms   Check Tcpdump Done    &{local_cpe}[minion_id]    &{local_cpe}[internet_if]
    wait until keyword succeeds  ${wait_to}    500ms   Check Tcpdump Done    &{remote_cpe}[minion_id]    &{remote_cpe}[internet_if]
    switch connection   ${sess_local_cpe}
    wait until keyword succeeds  3s     100ms   Check Capture Packets     local   /tmp/&{local_cpe}[internet_if].pcap  ${pkts_num}     &{local_cpe}[passwd]
    switch connection   ${sess_remote_cpe}
    wait until keyword succeeds  3s     100ms   Check Capture Packets     remote   /tmp/&{remote_cpe}[internet_if].pcap  ${pkts_num}     &{remote_cpe}[passwd]

Tcpdump Capture on Series with FileSize Specified
    [Tags]    Series  SDWANDEV-2036
    ${wait_to}=     evaluate  ${default_time}+10
    switch connection   ${sess_salt_master_async}
    Start CPE Tcpdump Async    &{local_cpe}[minion_id]    &{local_cpe}[internet_if]   ${default_time}   ${file_size}
    Start CPE Tcpdump Async    &{remote_cpe}[minion_id]    &{remote_cpe}[internet_if]   ${default_time}   ${file_size}
    switch connection   ${sess_salt_master}
    wait until keyword succeeds  ${wait_to}    500ms   Check Tcpdump Done    &{local_cpe}[minion_id]    &{local_cpe}[internet_if]
    wait until keyword succeeds  ${wait_to}    500ms   Check Tcpdump Done    &{remote_cpe}[minion_id]    &{remote_cpe}[internet_if]
    switch connection   ${sess_local_cpe}
    wait until keyword succeeds  3s     100ms   Check Capture FileSize     local   /tmp/&{local_cpe}[internet_if].pcap
    switch connection   ${sess_remote_cpe}
    wait until keyword succeeds  3s     100ms   Check Capture FileSize     remote   /tmp/&{remote_cpe}[internet_if].pcap

PCapture on Series with Time Specified and Fetch the File
    [Tags]    Series     SDWANDEV-2437   SDWANDEV-2475
    switch connection   ${sess_salt_master}
    Start PCap   &{local_cpe}[minion_id]    &{local_cpe}[internet_if]    ${0}   ${file_size}  ${capture_time}
    Start PCap   &{local_cpe}[minion_id]    &{local_cpe}[lan_if]    ${0}   ${file_size}  ${capture_time}
    Start PCap   &{remote_cpe}[minion_id]    &{remote_cpe}[internet_if]    ${0}   ${file_size}  ${capture_time}
    Start PCap   &{remote_cpe}[minion_id]    &{remote_cpe}[lan_if]    ${0}   ${file_size}  ${capture_time}
    wait until keyword succeeds  ${capture_time}   1   Check Pcapture Done   &{local_cpe}[minion_id]    &{local_cpe}[internet_if]
    wait until keyword succeeds  ${capture_time}   1   Check Pcapture Done   &{local_cpe}[minion_id]    &{local_cpe}[lan_if]
    wait until keyword succeeds  ${capture_time}   1   Check Pcapture Done   &{remote_cpe}[minion_id]    &{remote_cpe}[internet_if]
    wait until keyword succeeds  ${capture_time}   1   Check Pcapture Done   &{remote_cpe}[minion_id]    &{remote_cpe}[lan_if]
    ${res}  Fetch PCapture File     &{local_cpe}[minion_id]     &{local_cpe}[internet_if]
    should contain  ${res}  True
    ${res}  Fetch PCapture File     &{remote_cpe}[minion_id]     &{remote_cpe}[internet_if]
    should contain  ${res}  True
    ${res}  Fetch PCapture File     &{local_cpe}[minion_id]     &{local_cpe}[lan_if]
    should contain  ${res}  True
    ${res}  Fetch PCapture File     &{remote_cpe}[minion_id]     &{remote_cpe}[lan_if]
    should contain  ${res}  True
    switch connection   ${sess_local_cpe}
    Check Capture Time     local   ${pcap_folder}&{local_cpe}[internet_if].pcap  ${capture_time}     &{local_cpe}[passwd]
    switch connection   ${sess_remote_cpe}
    Check Capture Time     remote   ${pcap_folder}&{remote_cpe}[internet_if].pcap  ${capture_time}     &{remote_cpe}[passwd]

PCapture on Series with FileSize Specified
    [Tags]    Series     SDWANDEV-2438
    switch connection   ${sess_salt_master}
    Start PCap   &{local_cpe}[minion_id]    &{local_cpe}[internet_if]    ${0}   ${file_size}   ${default_time}
    Start PCap   &{remote_cpe}[minion_id]    &{remote_cpe}[internet_if]    ${0}   ${file_size}   ${default_time}
    wait until keyword succeeds  ${default_time}   1   Check Pcapture Done   &{local_cpe}[minion_id]    &{local_cpe}[internet_if]
    wait until keyword succeeds  ${default_time}   1   Check Pcapture Done   &{remote_cpe}[minion_id]    &{remote_cpe}[internet_if]
    switch connection  ${sess_local_cpe}
    wait until keyword succeeds  15s     100ms   Check Capture FileSize     local   ${pcap_folder}&{local_cpe}[internet_if].pcap
    switch connection  ${sess_remote_cpe}
    wait until keyword succeeds  5s     100ms   Check Capture FileSize     remote   ${pcap_folder}&{remote_cpe}[internet_if].pcap

*** Keywords ***
Setup
    #${wait}=     evaluate  ${capture_time}+10
    #set suite variable   ${wait_to}  ${wait}
    ${sess}=    SSH Login Salt Master
    set suite variable   ${sess_salt_master_async}    ${sess}
    ${sess}=    SSH Login Salt Master
    set suite variable   ${sess_salt_master}    ${sess}
    Check Accepted Salt Key    &{local_cpe}[minion_id]
    Check Accepted Salt Key    &{remote_cpe}[minion_id]
    Salt Connection Test    &{local_cpe}[minion_id]
    Salt Connection Test    &{remote_cpe}[minion_id]
    ssh_cpe  local   sess_local_cpe
    write sudo cmd   rm -rf /tmp/*.pcap    &{local_cpe}[passwd]
    set suite variable   ${sess_local_cpe}  sess_local_cpe
    ssh_cpe  remote  sess_remote_cpe
    write sudo cmd   rm -rf /tmp/*.pcap    &{remote_cpe}[passwd]
    set suite variable   ${sess_remote_cpe}  sess_remote_cpe
