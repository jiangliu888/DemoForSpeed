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
${filter_port}   ${6868}

*** Test Cases ***
Get CPE Ports Info
    [Tags]  Gateway     SDWANDEV-2063
    switch connection   ${sess_salt_master}
    ${salt_res}=     Get CPE Ports   &{guangzhou_cpe}[minion_id]
    ${salt_ports}=  get lines matching regexp   ${salt_res}  [a-z0-9]*
    switch connection   ${sess_guangzhou_cpe}
    write   ifconfig | grep -v ^[[:space:]] | grep -v ^$| awk '{print $1}'
    ${ifconfig_res}=    read until prompt
    ${ifconfig_ports}=  get lines matching regexp   ${ifconfig_res}  [a-z0-9]*
    should be equal  ${salt_ports}    ${ifconfig_ports}

Tcpdump Capture on Gateway with Time Specified
    [Tags]    Gateway     SDWANDEV-1977    SDWANDEV-2030    SDWANDEV-2110
    ${wait_to}=     evaluate  ${capture_time}+10
    switch connection   ${sess_salt_master_async}
    Start CPE Tcpdump Async    &{guangzhou_cpe}[minion_id]    &{guangzhou_cpe}[internet_if],&{guangzhou_cpe}[lan_if]   timeout=${capture_time}
    ssh login guangzhou
    write   ping -i 0.2 -t ${capture_time} &{nanjing_pc}[inner_ip] &
    switch connection   ${sess_salt_master}
    wait until keyword succeeds  ${wait_to}    500ms   Check Tcpdump Done    &{guangzhou_cpe}[minion_id]    &{guangzhou_cpe}[internet_if]
    wait until keyword succeeds  ${wait_to}    500ms   Check Tcpdump Done    &{guangzhou_cpe}[minion_id]    &{guangzhou_cpe}[lan_if]
    switch connection  ${sess_guangzhou_cpe}
    wait until keyword succeeds      2s  100ms   Check File Exists   /tmp/&{guangzhou_cpe}[internet_if].pcap
    wait until keyword succeeds      2s  100ms   Check File Exists   /tmp/&{guangzhou_cpe}[lan_if].pcap
    Check Capture Time     guangzhou   /tmp/&{guangzhou_cpe}[internet_if].pcap  ${capture_time}     &{guangzhou_cpe}[passwd]
    Check Capture Time     guangzhou   /tmp/&{guangzhou_cpe}[lan_if].pcap  ${capture_time}     &{guangzhou_cpe}[passwd]

Tcpdump Capture by Filter with Time Specified
    [Tags]    Gateway     SDWANDEV-2238
    switch connection   ${sess_salt_master}
    ${res}=     Start CPE Tcpdump Sync    &{guangzhou_cpe}[minion_id]    &{guangzhou_cpe}[internet_if]   ${capture_time}   ${None}  -c 5 port ${filter_port} and host &{local_pop}[ip2]
    should contain  ${res}   5 packets captured
    switch connection  ${sess_guangzhou_cpe}
    wait until keyword succeeds  3s    0.5s   Check GW Filter Capture      /tmp/&{guangzhou_cpe}[internet_if].pcap    5

Get Specified Pcap Files
    [Tags]      Gateway     SDWANDEV-2134
    switch connection  ${sess_guangzhou_cpe}
    Check FileSize  guangzhou   &{guangzhou_cpe}[internet_if].pcap
    switch connection   ${sess_salt_master}
    ${res}=     Get Captured File    &{guangzhou_cpe}[minion_id]    &{guangzhou_cpe}[internet_if]
    should contain  ${res}  &{guangzhou_cpe}[internet_if].pcap
    should contain  ${res}  True
    should not contain  ${res}  abc.pcap

Get All Pcap Files
    [Tags]      Gateway     SDWANDEV-2033
    switch connection  ${sess_guangzhou_cpe}
    wait until keyword succeeds    2s  100ms   Check File Exists   /tmp/&{guangzhou_cpe}[internet_if].pcap
    wait until keyword succeeds    2s  100ms   Check File Exists   /tmp/&{guangzhou_cpe}[lan_if].pcap
    Check FileSize  guangzhou   &{guangzhou_cpe}[internet_if].pcap
    Check FileSize  guangzhou   &{guangzhou_cpe}[lan_if].pcap
    switch connection   ${sess_salt_master}
    ${res}=     Get Captured File    &{guangzhou_cpe}[minion_id]    all
    should contain  ${res}  &{guangzhou_cpe}[internet_if].pcap
    should contain  ${res}  &{guangzhou_cpe}[lan_if].pcap
    should contain  ${res}  True
    should not contain  ${res}  abc.pcap

Tcpdump Capture on Gateway with Packets Specified
    [Tags]    Gateway     SDWANDEV-2035
    switch connection   ${sess_salt_master}
    Check Accepted Salt Key    &{guangzhou_cpe}[minion_id]
    ${res_wan}=     Start CPE Tcpdump Sync    &{guangzhou_cpe}[minion_id]    &{guangzhou_cpe}[internet_if]   ${default_time}   ${None}    -c ${pkts_num}
    should contain  ${res_wan}     ${pkts_num} packets captured
    switch connection   ${sess_guangzhou_cpe}
    Check Capture Packets     guangzhou   /tmp/&{guangzhou_cpe}[internet_if].pcap  ${pkts_num}     &{guangzhou_cpe}[passwd]

Tcpdump Capture on Gateway with FileSize Specified
    [Tags]    Gateway     SDWANDEV-2036
    switch connection   ${sess_guangzhou_pc}
    write   ping -M do -s 1024 -i 0.2 -t ${capture_time} &{nanjing_pc}[inner_ip] &
    switch connection   ${sess_salt_master}
    ${res_wan}=     Start CPE Tcpdump Sync    &{guangzhou_cpe}[minion_id]    &{guangzhou_cpe}[internet_if]   ${default_time}   ${file_size}
    should contain  ${res_wan}     Exceeded file size limit
    switch connection   ${sess_guangzhou_cpe}
    Check Capture FileSize     guangzhou   /tmp/&{guangzhou_cpe}[internet_if].pcap

Wrong Nic for Salt Tcpdump
    [Tags]    Gateway     SDWANDEV-2037
    switch connection   ${sess_salt_master}
    ${res}=    Start CPE Tcpdump Sync    &{guangzhou_cpe}[minion_id]    eth9
    should contain  ${res}  No such device exists

Get Pcap File Before Tcpdump Done
    [Tags]  Gateway     SDWANDEV-2114
    ${wait_to}=     evaluate  ${capture_time}+10
    switch connection   ${sess_salt_master_async}
    Start CPE Tcpdump Async    &{guangzhou_cpe}[minion_id]    &{guangzhou_cpe}[internet_if]   timeout=${capture_time}
    switch connection   ${sess_salt_master}
    ${res}=     Get Captured File    &{guangzhou_cpe}[minion_id]    &{guangzhou_cpe}[internet_if]
    should contain  ${res}  is Running
    [Teardown]  wait until keyword succeeds  ${wait_to}    500ms   Check Tcpdump Done    &{guangzhou_cpe}[minion_id]    &{guangzhou_cpe}[internet_if]

Reject Salt PCapture Request
    [Tags]  Gateway     SDWANDEV-2443
    switch connection   ${sess_salt_master}
    ${status}   ${res}=    run keyword and ignore error  Start PCap   &{guangzhou_cpe}[minion_id]    &{guangzhou_cpe}[internet_if]    ${0}   ${1024}
    should contain   ${res}   gateway is not supported

*** Keywords ***
Setup
    #${wait}=     evaluate  ${capture_time}+10
    #set suite variable   ${wait_to}  ${wait}
    ${sess}=    SSH Login Salt Master
    set suite variable   ${sess_salt_master_async}    ${sess}
    ${sess}=    SSH Login Salt Master
    set suite variable   ${sess_salt_master}    ${sess}
    Check Accepted Salt Key    &{guangzhou_cpe}[minion_id]
    Salt Connection Test    &{guangzhou_cpe}[minion_id]
    ssh_cpe  guangzhou   sess_guangzhou_cpe
    set suite variable   ${sess_guangzhou_cpe}    sess_guangzhou_cpe
    write openwrt cmd    rm -rf /tmp/*.pcap     &{guangzhou_cpe}[passwd]
    write openwrt cmd     touch /tmp/abc.pcap          &{guangzhou_cpe}[passwd]
    ssh_pc  guangzhou   sess_guangzhou_pc
    set suite variable   ${sess_guangzhou_pc}    sess_guangzhou_pc

Check FileSize
    [Arguments]  ${cpe}  ${file}
    write   ls -ltr /tmp/${file} | awk '{print $5}'
    ${res}=    read until prompt
    ${size}    Get Line    ${res}    0
    Should Be True    ${size} > 0

Check GW Filter Capture
    [Arguments]    ${captured_file}    ${pkts_num}
    write   tcpdump -n -# -r ${captured_file} | grep -E "VXLAN|UDP" | wc -l
    ${res}=     read until prompt
    ${num}=    get lines matching regexp    ${res}   \\d+
    should be true   ${num} == ${pkts_num}
    write   tcpdump -n -r ${captured_file} | grep 99[0-9] | wc -l
    ${res}=     read until prompt
    ${num}=    get lines matching regexp    ${res}   \\d+
    should be true   ${num} == ${pkts_num}
