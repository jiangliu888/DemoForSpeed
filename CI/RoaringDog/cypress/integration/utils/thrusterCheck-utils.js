
import {getIdByCompanyName, getIdBySiteName, getSiteNEidByName} from '../utils/basic-utils'
import {exec_cmd_on_local} from '../utils/consulCheck-utils'
import {testCPEGlobalConfigBody} from '../utils/variables-utils'
const pythonLogPath = "cypress/results/pythoncmd.log"
const genFilesPath = "/tmp/"

export function checkAiwanJson(token, companyName, siteName, sn){
  let tmpFile = 'aiwan.json'
  getIdByCompanyName(token, companyName)
  cy.get('@companyId').then(companyId => {
    expect(companyId).to.not.equal("")
    getSiteNEidByName(token,companyId, siteName)
    cy.get('@neId').then(neId => {
        getIdBySiteName(token, companyId, siteName)
        cy.get('@siteId').then(siteId => {
            expect(neId).to.not.equal("")
            cy.writeFile(genFilesPath + tmpFile, "{\n\t\"neId\": " + neId + "\n}")
            let cmd = "diff " + genFilesPath + tmpFile + ' ' + genFilesPath + sn + "/" + tmpFile
            exec_cmd_on_local(cmd)
        })
    })
  })
}

export function checkInfoJson(token, companyName, siteName, sn){
  let tmpFile = 'info.json'
  getIdByCompanyName(token, companyName)
  cy.get('@companyId').then(companyId => {
    expect(companyId).to.not.equal("")
    getSiteNEidByName(token,companyId, siteName)
    cy.get('@neId').then(neId => {
        getIdBySiteName(token, companyId, siteName)
        cy.get('@siteId').then(siteId => {
            expect(neId).to.not.equal("")
            var infoCheck = {}
            infoCheck.company = companyId
            infoCheck.siteId = siteId
            infoCheck.siteName = siteName
            infoCheck.companyName = companyName
            cy.log(JSON.stringify(infoCheck))
            cy.writeFile(genFilesPath + tmpFile, JSON.stringify(infoCheck))
            let cmd = "export PYTHONPATH=../erlang;python cypress/integration/utils/python-util/CheckConsul.py \"['checkJsonFile']\" " + genFilesPath + tmpFile + ' ' + genFilesPath + sn + "/" + tmpFile
            exec_cmd_on_local(cmd)
        })
    })
  })
}

export function checkNeJson(sn){
  let tmpFile = 'ne.json'
  let neBody = JSON.parse(JSON.stringify(testCPEGlobalConfigBody.ST))
  neBody.controllers[0].mode = "gateway"
  neBody.controllers[1].mode = "parallel"
  neBody.controllers[2].mode = "series"
  cy.log(neBody.controllers[2].mode)
  cy.writeFile(genFilesPath + tmpFile, neBody)
  let cmd = "diff --suppress-common-lines -wy " + genFilesPath + tmpFile + ' ' + genFilesPath + sn + "/" + tmpFile
  exec_cmd_on_local(cmd)
}

export function checkStartupJson(site, sn, master=true){
  let tmpFile = 'startup_cpe.json'
  var siteCheck = {}
  let mode = ""
  switch (site.type) {
      case "网关":
        mode = "gateway"
        break;
      case "串联":
        mode = "series"
        break;
      case "旁挂":
        mode = "parallel"
        break;
      default:
        cy.log("Unknown type: " + site.type)
  }
  siteCheck.mode = mode
  siteCheck.tunnelPort = parseInt(site.tunnelNum)
  var interfaces = new Array()
  if (mode != "parallel") {
    var i
    for (i=0;i<site.wans.length;i++){
      var interfaceWan = {}
      interfaceWan.name = site.wans[i].ifname
      interfaceWan.type = "WAN"
      interfaceWan.mode = site.wans[i].ip_mode
      interfaceWan.proxy = site.wans[i].proxy
      interfaceWan.usage = "normal"
      if (site.wans[i].hasOwnProperty('gatewayMac')) {
        interfaceWan["gw-mac"] = site.wans[i].gatewayMac
      }
      if (site.wans[i].hasOwnProperty('staticIp') && site.wans[i].staticIp != "") {
        interfaceWan["static-ip"] = site.wans[i].staticIp
      }
      interfaces.push(interfaceWan)
    }
    if (site.lans[0].IDC == true) {
        var interfaceLan = {}
        interfaceLan.name = site.lans[0].ifname
        interfaceLan.type = "LAN"
        interfaceLan.mode = site.lans[0].ip_mode
        interfaceLan.pair = site.lans[0].pair
        interfaces.push(interfaceLan)
    }
    if (site.hasOwnProperty('enablePrivate') && site.enablePrivate == true) {
        var interfaceDIA = {"name":"enp1s0f2","type":"LAN","mode":"DIA"}
        interfaces.push(interfaceDIA)
    }
  } else {
    // WAN
    var interfaceWan = {}
    interfaceWan.name = site.wans[0].ifname
    interfaceWan.type = "WAN"
    interfaceWan.mode = site.wans[0].ip_mode
    interfaceWan.proxy = true
    interfaceWan.usage = "normal"
    interfaceWan["parallel-gateway"] = site.wans[0].gateway
    var wanIps = new Array()
    for (i=0;i<site.wans.length;i++) {
      var wanIp = {}
      wanIp["parallel-ip"] = site.wans[i].ip
      wanIp["parallel-netmask"] = site.wans[i].mask
      wanIp["ip-mode"] = site.wans[i].ip_mode
      wanIps.push(wanIp)
    }
    interfaceWan.ips = wanIps
    if (site.HA == true) {
      if (master == true) {
        interfaceWan["static-ip"] = site.HAaddress.master_wanip
      } else {
        interfaceWan["static-ip"] = site.HAaddress.standby_wanip
      }
    }
    interfaces.push(interfaceWan)
    // LAN
    var interfaceLan = {}
    interfaceLan.name = site.lans[0].ifname
    interfaceLan.type = "LAN"
    interfaceLan.mode = "FIA"
    interfaceLan.pair = site.wans[0].ifname
    interfaceLan["parallel-gateway"] = site.lans[0].gateway
    var lanIps = new Array()
    var lanIp = {}
    lanIp["parallel-ip"] = site.lans[0].ip_addr
    lanIp["parallel-netmask"] = site.lans[0].mask
    lanIp["ip-mode"] = "FIA"
    lanIps.push(lanIp)
    interfaceLan.ips = lanIps
    if (site.HA == true) {
      if (master == true) {
        interfaceLan["static-ip"] = site.HAaddress.master_lanip
      } else {
        interfaceLan["static-ip"] = site.HAaddress.master_lanip
      }
    }
    interfaces.push(interfaceLan)
  }
  siteCheck.interface = interfaces
  if (site.hasOwnProperty('natNet')) {
    siteCheck.natNet = site.natNet
  }
  siteCheck.reportInterval = parseInt(site.reportInterval)
  siteCheck.scoreInterval = parseInt(site.scoreInterval)
  cy.log(JSON.stringify(siteCheck))
  cy.writeFile(genFilesPath + tmpFile, JSON.stringify(siteCheck))
  let cmd = "export PYTHONPATH=../erlang;python cypress/integration/utils/python-util/CheckConsul.py \"['checkJsonFile']\" " + genFilesPath + tmpFile + ' ' + genFilesPath + site.sn + "/" + tmpFile
  exec_cmd_on_local(cmd)
}

export function checkWirelessJson(site, sn) {
  let tmpFile = 'wireless'
  cy.writeFile(genFilesPath + tmpFile, "##s\n")
  if (site.type == '网关') {
    cy.writeFile(genFilesPath + tmpFile, "config wifi-iface 'default_radio0'\n", {flag: 'a+'})
    cy.writeFile(genFilesPath + tmpFile, "\toption ssid '" + site.wifi.ssid + "'\n", {flag: 'a+'})
    cy.writeFile(genFilesPath + tmpFile, "\toption encryption '" + site.wifi.encryption + "'\n", {flag: 'a+'})
    cy.writeFile(genFilesPath + tmpFile, "\toption key '" + site.wifi.key + "'\n", {flag: 'a+'})
    var net_name = (site.wifi.network == 'lan1')?"lan":site.wifi.network.toLowerCase()
    cy.writeFile(genFilesPath + tmpFile, "\toption network '" + net_name + "'\n", {flag: 'a+'})
    cy.writeFile(genFilesPath + tmpFile, "\toption macfilter '" + site.wifi.macfilter + "'\n", {flag: 'a+'})
    var i
    for (i=0;i<site.wifi.mac_list.length;i++) {
      cy.writeFile(genFilesPath + tmpFile, "\tlist maclist '" + site.wifi.mac_list[i] + "'\n", {flag: 'a+'})
    }
    cy.writeFile(genFilesPath + tmpFile, "\toption device 'radio0'\n", {flag: 'a+'})
    cy.writeFile(genFilesPath + tmpFile, "\toption mode 'ap'\n", {flag: 'a+'})
    cy.writeFile(genFilesPath + tmpFile, "\toption disabled '0'\n\n", {flag: 'a+'})
  }
  cy.writeFile(genFilesPath + tmpFile, "\n##e\n\n", {flag: 'a+'})
  let cmd = "diff " + genFilesPath + tmpFile + ' ' + genFilesPath + site.sn + "/" + tmpFile
  exec_cmd_on_local(cmd)
}

export function checkFirewallJson(site, sn) {
  let tmpFile = 'firewall'
  cy.writeFile(genFilesPath + tmpFile, "##s\n")
  if (site.type == '网关') {
    if (site.hasOwnProperty('natPort')) {
      cy.writeFile(genFilesPath + tmpFile, "config rule\n", {flag: 'a+'})
      cy.writeFile(genFilesPath + tmpFile, "\toption name 'Allow-Aiwan-Link'\n", {flag: 'a+'})
      cy.writeFile(genFilesPath + tmpFile, "\toption src 'wan'\n", {flag: 'a+'})
      cy.writeFile(genFilesPath + tmpFile, "\toption proto 'udp'\n", {flag: 'a+'})
      cy.writeFile(genFilesPath + tmpFile, "\toption dest_port '" + site.natPort + "'\n", {flag: 'a+'})
      cy.writeFile(genFilesPath + tmpFile, "\toption target 'ACCEPT'\n", {flag: 'a+'})
      cy.writeFile(genFilesPath + tmpFile, "\t option family 'ipv4'\n", {flag: 'a+'})
    }
    var i
    for (i=0;i<site.lans.length;i++) {
      cy.writeFile(genFilesPath + tmpFile, "config zone\n", {flag: 'a+'})
      var lan_name = (site.lans[i].name == 'LAN1')?"lan":'aiwanlan2'
      cy.writeFile(genFilesPath + tmpFile, "\toption name '" + lan_name + "'\n", {flag: 'a+'})
      cy.writeFile(genFilesPath + tmpFile, "\tlist network '" + lan_name + "'\n", {flag: 'a+'})
      cy.writeFile(genFilesPath + tmpFile, "\toption input 'ACCEPT'\n", {flag: 'a+'})
      cy.writeFile(genFilesPath + tmpFile, "\toption output 'ACCEPT'\n", {flag: 'a+'})
      cy.writeFile(genFilesPath + tmpFile, "\toption forward 'REJECT'\n", {flag: 'a+'})
      if (site.lans[i].IDC) {
        cy.writeFile(genFilesPath + tmpFile, "config forwarding\n", {flag: 'a+'})
        cy.writeFile(genFilesPath + tmpFile, "\toption src '" + lan_name + "'\n", {flag: 'a+'})
        cy.writeFile(genFilesPath + tmpFile, "\toption dest 'aiwan_tun'\n\n", {flag: 'a+'})
        cy.writeFile(genFilesPath + tmpFile, "config forwarding\n", {flag: 'a+'})
        cy.writeFile(genFilesPath + tmpFile, "\toption src 'aiwan_tun'\n", {flag: 'a+'})
        cy.writeFile(genFilesPath + tmpFile, "\toption dest '" + lan_name + "'\n\n", {flag: 'a+'})
      }
      if (site.lans[i].internet) {
        cy.writeFile(genFilesPath + tmpFile, "config forwarding\n", {flag: 'a+'})
        cy.writeFile(genFilesPath + tmpFile, "\toption src '" + lan_name + "'\n", {flag: 'a+'})
        cy.writeFile(genFilesPath + tmpFile, "\toption dest 'wan'\n\n", {flag: 'a+'})
      }
    }
  }
  cy.writeFile(genFilesPath + tmpFile, "\n##e\n\n", {flag: 'a+'})
  let cmd = "diff " + genFilesPath + tmpFile + ' ' + genFilesPath + site.sn + "/" + tmpFile
  exec_cmd_on_local(cmd)
}

export function checkNetworkJson(site, sn) {
  let tmpFile = 'network'
  cy.writeFile(genFilesPath + tmpFile, "##s\n")
  if (site.type == '网关') {
    var i
    for (i=0;i<site.wans.length;i++) {
      cy.writeFile(genFilesPath + tmpFile, "config interface '", {flag: 'a+'})
      var wan_name = (site.wans[i].name == 'WAN1')?"wan":site.wans[i].name.toLowerCase()
      cy.writeFile(genFilesPath + tmpFile, wan_name + "'\n", {flag: 'a+'})
      cy.writeFile(genFilesPath + tmpFile, "\toption ifname '" + site.wans[i].ifname + "'\n", {flag: 'a+'})
      cy.writeFile(genFilesPath + tmpFile, "\toption proto '", {flag: 'a+'})
      switch (site.wans[i].ip_type) {
          case "静态ip地址":
            cy.writeFile(genFilesPath + tmpFile, "static'\n\toption ipaddr '" + site.wans[i].ip + "'\n", {flag: 'a+'})
            var maskStr=ipv4PrefixLen2MaskStr(site.wans[i].mask)
            cy.writeFile(genFilesPath + tmpFile, "\toption netmask '" + maskStr + "'\n\n", {flag: 'a+'})
            break
          case "PPPOE":
            cy.writeFile(genFilesPath + tmpFile, "pppoe'\n\toption username '" + site.wans[i].account + "'\n", {flag: 'a+'})
            cy.writeFile(genFilesPath + tmpFile, "\toption password '" + site.wans[i].password + "'\n", {flag: 'a+'})
            cy.writeFile(genFilesPath + tmpFile, "\toption metric '100'\n\n", {flag: 'a+'})
            break
          case "DHCP":
            cy.writeFile(genFilesPath + tmpFile, "dhcp'\n\n", {flag: 'a+'})
            break
          default:
            cy.log("Unknown ip_type: " + site.wans[i].ip_type)
      }
    }
    for (i=0;i<site.lans.length;i++) {
      cy.writeFile(genFilesPath + tmpFile, "config interface '", {flag: 'a+'})
      var lan_name = (site.lans[i].name == 'LAN1')?"lan":"aiwanlan2"
      cy.writeFile(genFilesPath + tmpFile, lan_name + "'\n", {flag: 'a+'})
      cy.writeFile(genFilesPath + tmpFile, "\toption ifname '" + site.lans[i].phy_ifname + "'\n", {flag: 'a+'})
      cy.writeFile(genFilesPath + tmpFile, "\toption proto '", {flag: 'a+'})
      cy.writeFile(genFilesPath + tmpFile, "static'\n\toption ipaddr '" + site.lans[i].ip_addr + "'\n", {flag: 'a+'})
      var maskStr=ipv4PrefixLen2MaskStr(site.lans[i].mask)
      cy.writeFile(genFilesPath + tmpFile, "\toption netmask '" + maskStr + "'\n", {flag: 'a+'})
      cy.writeFile(genFilesPath + tmpFile, "\toption type 'bridge'\n\n", {flag: 'a+'})
    }
  }
  // wan2 static
  for (i=1;i<site.wans.length;i++) {
      if (site.wans[i].ip_type == '静态ip地址') {
          cy.writeFile(genFilesPath + tmpFile, "config route 'to_gateway_default_", {flag: 'a+'})
          var wan_name = (site.wans[i].name == 'WAN1')?"wan":site.wans[i].name.toLowerCase()
          cy.writeFile(genFilesPath + tmpFile, wan_name + "'\n", {flag: 'a+'})
          cy.writeFile(genFilesPath + tmpFile, "\toption interface '" + wan_name + "'\n", {flag: 'a+'})
          cy.writeFile(genFilesPath + tmpFile, "\toption table '20'\n", {flag: 'a+'})
          cy.writeFile(genFilesPath + tmpFile, "\toption netmask '0.0.0.0'\n", {flag: 'a+'})
          cy.writeFile(genFilesPath + tmpFile, "\toption target '0.0.0.0'\n", {flag: 'a+'})
          cy.writeFile(genFilesPath + tmpFile, "\toption gateway '" + site.wans[i].gateway + "'\n\n", {flag: 'a+'})
          cy.writeFile(genFilesPath + tmpFile, "config route 'to_gateway_default_main_" + wan_name + "'\n", {flag: 'a+'})
          cy.writeFile(genFilesPath + tmpFile, "\toption interface '" + wan_name + "'\n", {flag: 'a+'})
          cy.writeFile(genFilesPath + tmpFile, "\toption table 'main'\n", {flag: 'a+'})
          cy.writeFile(genFilesPath + tmpFile, "\toption netmask '0.0.0.0'\n", {flag: 'a+'})
          cy.writeFile(genFilesPath + tmpFile, "\toption target '0.0.0.0'\n", {flag: 'a+'})
          cy.writeFile(genFilesPath + tmpFile, "\toption gateway '" + site.wans[i].gateway + "'\n", {flag: 'a+'})
          cy.writeFile(genFilesPath + tmpFile, "\toption metric '100'\n\n", {flag: 'a+'})
      }
  }
  cy.writeFile(genFilesPath + tmpFile, "\n##e\n", {flag: 'a+'})
  cy.writeFile(genFilesPath + tmpFile, "\n##rs\n", {flag: 'a+'})
  if (site.hasOwnProperty('natNet')) {
    cy.writeFile(genFilesPath + tmpFile, "config route\n", {flag: 'a+'})
    cy.writeFile(genFilesPath + tmpFile, "\toption interface 'tun'\n", {flag: 'a+'})
    var natNet = site.natNet.split('/')
    cy.writeFile(genFilesPath + tmpFile, "\toption target '" + natNet[0] + "'\n", {flag: 'a+'})
    cy.writeFile(genFilesPath + tmpFile, "\toption netmask '" + ipv4PrefixLen2MaskStr(natNet[1]) + "'\n\n", {flag: 'a+'})
  }
  cy.writeFile(genFilesPath + tmpFile, "\n##re\n", {flag: 'a+'})
  let cmd = "diff " + genFilesPath + tmpFile + ' ' + genFilesPath + site.sn + "/" + tmpFile
  exec_cmd_on_local(cmd)
}

export function checkDhcpJson(site, sn) {
  let tmpFile = 'dhcp'
  cy.writeFile(genFilesPath + tmpFile, "##s\n")
  var i
  for (i=0;i<site.lans.length;i++) {
    var if_name = (site.lans[i].name == 'LAN1')?"lan":site.lans[i].name.toLowerCase()
    var lan_name = (site.lans[i].name == 'LAN1')?"lan":"aiwanlan2"
    cy.writeFile(genFilesPath + tmpFile, "config dhcp '" + if_name + "'\n", {flag: 'a+'})
    if (site.lans[i].DHCP==false) {
        cy.writeFile(genFilesPath + tmpFile, "\toption dhcpv4 'disable'\n\n", {flag: 'a+'})
    } else {
      cy.writeFile(genFilesPath + tmpFile, "\toption interface '" + lan_name + "'\n", {flag: 'a+'})
      cy.writeFile(genFilesPath + tmpFile, "\toption start '" + site.lans[i].ip_start.split('.').pop() + "'\n", {flag: 'a+'})
      var count=site.lans[i].ip_end.split('.').pop()-site.lans[i].ip_start.split('.').pop()
      cy.writeFile(genFilesPath + tmpFile, "\toption limit '" + count + "'\n", {flag: 'a+'})
      cy.writeFile(genFilesPath + tmpFile, "\toption leasetime '12h'\n", {flag: 'a+'})
      cy.writeFile(genFilesPath + tmpFile, "\toption dhcpv6 'server'\n", {flag: 'a+'})
      cy.writeFile(genFilesPath + tmpFile, "\toption ra 'server'\n\n", {flag: 'a+'})
    }
  }
  cy.writeFile(genFilesPath + tmpFile, "\n##e\n\n", {flag: 'a+'})
  let cmd = "diff " + genFilesPath + tmpFile + ' ' + genFilesPath + site.sn + "/" + tmpFile
  exec_cmd_on_local(cmd)
}

export function ipv4PrefixLen2MaskStr (prefixLen) {
  if (prefixLen > 32) {
    return '255.255.255.255'
  }
  var x=prefixLen/8
  var y=prefixLen%8
  var z=4-x-1
  var res=""
  var i
  for (i=0;i<x;i++) {
    res=res.concat('255.')
  }
  var tmp=0
  for (i=0;i<y;i++) {
    tmp=tmp*2+1
  }
  for (i=0;i<8-y;i++) {
    tmp=tmp*2
  }
  res=res.concat(tmp + '.')
  for (i=0;i<z;i++) {
    res=res.concat('0.')
  }
  return res.substring(0,res.length-1)
}

export function exec_cmd_on_local_ignoreErr(cmd){
  cy.log(cmd)
  cy.exec(cmd,{ failOnNonZeroExit: false }).then(result => {
    cy.writeFile(pythonLogPath,cmd + "\ncmdError:\n" + result.stderr + "\n" + result.stdout + "\n", {flag: 'a+'})
    cy.log(result.stderr)
    cy.log(result.stdout)
    cy.log(result.code)
  })
}
