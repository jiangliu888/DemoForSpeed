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
    [Tags]  Sideway     SDWANDEV-2063
    switch connection   ${sess_salt_master}
    ${salt_res}=     Get CPE Ports   &{wuhan_cpe}[minion_id]
    ${salt_ports}=  get lines matching regexp   ${salt_res}  [a-z0-9]*
    switch connection   ${sess_wuhan_cpe}
    write   ifconfig | grep -v ^[[:space:]] | grep -v ^$| awk '{print $1}'
    ${ifconfig_res}=    read until prompt
    ${ifconfig_ports}=  get lines matching regexp   ${ifconfig_res}  [a-z0-9]*
    should be equal  ${salt_ports}    ${ifconfig_ports}

Tcpdump Capture on Sideway with Time Specified
    [Tags]    Sideway     SDWANDEV-1977    SDWANDEV-1984
    ${wait_to}=     evaluate  ${capture_time}+10
    switch connection   ${sess_salt_master_async}
    #Start CPE Tcpdump Async    &{nanjing_cpe}[minion_id]    &{nanjing_cpe}[internet_if],&{nanjing_cpe}[lan_if]   timeout=${capture_time}
    Start CPE Tcpdump Async    &{wuhan_cpe}[minion_id]    &{wuhan_cpe}[internet_if]   timeout=${capture_time}
    Start CPE Tcpdump Async    &{wuhan_cpe}[minion_id]    &{wuhan_cpe}[lan_if]   timeout=${capture_time}
    switch connection   ${sess_salt_master}
    #wait until keyword succeeds  ${wait_to}    500ms   Check Tcpdump Done    &{nanjing_cpe}[minion_id]    &{nanjing_cpe}[internet_if]
    #wait until keyword succeeds  ${wait_to}    500ms   Check Tcpdump Done    &{nanjing_cpe}[minion_id]    &{nanjing_cpe}[lan_if]
    wait until keyword succeeds  ${wait_to}    500ms   Check Tcpdump Done    &{wuhan_cpe}[minion_id]    &{wuhan_cpe}[internet_if]
    wait until keyword succeeds  ${wait_to}    500ms   Check Tcpdump Done    &{wuhan_cpe}[minion_id]    &{wuhan_cpe}[lan_if]
    #switch connection    ${sess_nanjing_cpe}
    #Check Capture Time     nanjing   /tmp/&{nanjing_cpe}[internet_if].pcap  ${capture_time}     &{nanjing_cpe}[passwd]
    #Check Capture Time     nanjing   /tmp/&{nanjing_cpe}[lan_if].pcap  ${capture_time}     &{nanjing_cpe}[passwd]
    switch connection   ${sess_wuhan_cpe}
    Check Capture Time     wuhan   /tmp/&{wuhan_cpe}[internet_if].pcap  ${capture_time}     &{wuhan_cpe}[passwd]
    #Check Capture Time     wuhan   /tmp/&{wuhan_cpe}[lan_if].pcap  ${capture_time}     &{wuhan_cpe}[passwd]

Tcpdump Capture on Sideway with Packets Specified
    [Tags]    Sideway     SDWANDEV-2035
    ${wait_to}=     evaluate  ${default_time}+10
    switch connection   ${sess_salt_master_async}
    #Start CPE Tcpdump Async    &{nanjing_cpe}[minion_id]    &{nanjing_cpe}[internet_if]   ${default_time}   ${None}    -c ${pkts_num}
    Start CPE Tcpdump Async    &{wuhan_cpe}[minion_id]    &{wuhan_cpe}[internet_if]   ${default_time}   ${None}    -c ${pkts_num}
    switch connection   ${sess_salt_master}
    #wait until keyword succeeds  ${wait_to}    500ms   Check Tcpdump Done    &{nanjing_cpe}[minion_id]    &{nanjing_cpe}[internet_if]
    wait until keyword succeeds  ${wait_to}    500ms   Check Tcpdump Done    &{wuhan_cpe}[minion_id]    &{wuhan_cpe}[internet_if]
    #switch connection  ${sess_nanjing_cpe}
    #Check Capture Packets     nanjing   /tmp/&{nanjing_cpe}[internet_if].pcap  ${pkts_num}     &{nanjing_cpe}[passwd]
    switch connection   ${sess_wuhan_cpe}
    wait until keyword succeeds  3s     100ms   Check Capture Packets     wuhan   /tmp/&{wuhan_cpe}[internet_if].pcap  ${pkts_num}     &{wuhan_cpe}[passwd]

Tcpdump Capture on Sideway with FileSize Specified
    [Tags]    Sideway     SDWANDEV-2036
    ${wait_to}=     evaluate  ${default_time}+10
    switch connection   ${sess_salt_master_async}
    #Start CPE Tcpdump Async    &{nanjing_cpe}[minion_id]    &{nanjing_cpe}[internet_if]   ${default_time}   ${file_size}
    Start CPE Tcpdump Async    &{wuhan_cpe}[minion_id]    &{wuhan_cpe}[internet_if]   ${default_time}   ${file_size}
    switch connection   ${sess_salt_master}
    #wait until keyword succeeds  ${wait_to}    500ms   Check Tcpdump Done    &{nanjing_cpe}[minion_id]    &{nanjing_cpe}[internet_if]
    wait until keyword succeeds  ${wait_to}    500ms   Check Tcpdump Done    &{wuhan_cpe}[minion_id]    &{wuhan_cpe}[internet_if]
    #switch connection  ${sess_nanjing_cpe}
    #Check Capture FileSize     nanjing   /tmp/&{nanjing_cpe}[internet_if].pcap
    switch connection  ${sess_wuhan_cpe}
    wait until keyword succeeds  3s     100ms   Check Capture FileSize     wuhan   /tmp/&{wuhan_cpe}[internet_if].pcap

Reject Wrong Port Pcapture by Salt
    [Tags]    Sideway  SDWANDEV-2440
    switch connection   ${sess_salt_master}
    ${status}   ${res}=    run keyword and ignore error  Start PCap   &{wuhan_cpe}[minion_id]    eth10    ${0}   ${1024}  ${capture_time}
    should contain  ${res}  pcap err interface name

PCapture on Sideway with Time Specified and Fetch the File
    [Tags]    Sideway     SDWANDEV-2437   SDWANDEV-2475
    switch connection   ${sess_salt_master}
    Start PCap   &{wuhan_cpe}[minion_id]    &{wuhan_cpe}[internet_if]    ${0}   ${file_size}  ${capture_time}
    Start PCap   &{wuhan_cpe}[minion_id]    &{wuhan_cpe}[lan_if]    ${0}   ${file_size}  ${capture_time}
    wait until keyword succeeds  ${capture_time}   1   Check Pcapture Done   &{wuhan_cpe}[minion_id]    &{wuhan_cpe}[internet_if]
    wait until keyword succeeds  ${capture_time}   1   Check Pcapture Done   &{wuhan_cpe}[minion_id]    &{wuhan_cpe}[lan_if]
    ${res}  Fetch PCapture File     &{wuhan_cpe}[minion_id]     &{wuhan_cpe}[internet_if]
    should contain  ${res}  True
    ${res}  Fetch PCapture File     &{wuhan_cpe}[minion_id]     &{wuhan_cpe}[lan_if]
    should contain  ${res}  True
    switch connection   ${sess_wuhan_cpe}
    Check Capture Time     wuhan   ${pcap_folder}&{wuhan_cpe}[internet_if].pcap  ${capture_time}     &{wuhan_cpe}[passwd]

PCapture on Sideway with FileSize Specified
    [Tags]    Sideway     SDWANDEV-2438
    switch connection   ${sess_salt_master}
    Start PCap   &{wuhan_cpe}[minion_id]    &{wuhan_cpe}[internet_if]    ${0}   ${file_size}   ${default_time}
    wait until keyword succeeds  ${default_time}   1   Check Pcapture Done   &{wuhan_cpe}[minion_id]    &{wuhan_cpe}[internet_if]
    switch connection  ${sess_wuhan_cpe}
    wait until keyword succeeds  25s     100ms   Check Capture FileSize     wuhan   ${pcap_folder}&{wuhan_cpe}[internet_if].pcap

Reject Running Port Pcapture Start by Salt
    [Tags]    Sideway  SDWANDEV-2441
    ${timeout}=  evaluate  ${capture_time} + 5
    switch connection   ${sess_salt_master}
    Start PCap   &{wuhan_cpe}[minion_id]    &{wuhan_cpe}[internet_if]    ${0}   ${file_size}  ${capture_time}
    wait until keyword succeeds  5   100ms    check pcapture running      &{wuhan_cpe}[minion_id]    &{wuhan_cpe}[internet_if]
    ${status}   ${res}=    run keyword and ignore error  Start PCap   &{wuhan_cpe}[minion_id]    &{wuhan_cpe}[internet_if]    ${0}   ${1024}  ${capture_time}
    should contain   ${res}  pcap err busy
    [Teardown]  wait until keyword succeeds  ${timeout}   1   Check Pcapture Done   &{wuhan_cpe}[minion_id]    &{wuhan_cpe}[internet_if]

*** Keywords ***
Setup
    #${wait}=     evaluate  ${capture_time}+10
    #set suite variable   ${wait_to}  ${wait}
    ${sess}=    SSH Login Salt Master
    set suite variable   ${sess_salt_master_async}    ${sess}
    ${sess}=    SSH Login Salt Master
    set suite variable   ${sess_salt_master}    ${sess}
    #Check Accepted Salt Key    &{nanjing_cpe}[minion_id]
    Check Accepted Salt Key    &{wuhan_cpe}[minion_id]
    #Salt Connection Test    &{nanjing_cpe}[minion_id]
    Salt Connection Test    &{wuhan_cpe}[minion_id]
    ssh_cpe  wuhan   sess_wuhan_cpe
    set suite variable   ${sess_wuhan_cpe}  sess_wuhan_cpe
    write sudo cmd   rm -rf /tmp/*.pcap    &{wuhan_cpe}[passwd]
    #ssh_cpe  nanjing   sess_nanjing_cpe
    #set suite variable   ${sess_nanjing_cpe}  sess_nanjing_cpe
    #write sudo cmd   rm -rf /tmp/*.pcap    &{nanjing_cpe}[passwd]
