import re

from erlang.libs.common.SshUtil import SshUtil
from erlang.libs.variables import InterfacePathVariables as Temple


class UranusCli(object):
    flows_cmd = 'flows'
    set_cfg = 'cfg set '
    es_address = 'com.wsds.aiwan.uranus.gaea.provider.es.impl.EsProviderImpl aiwanEsUrls'
    area_selector_delay = 'com.wsds.aiwan.uranus.gaea.model.area.impl.AreaSelectorImpl areaSelectorDelay'
    net_measure_interval = 'com.wsds.aiwan.uranus.gaea.model.net.measure.impl.NetMeasureAssemblerImpl netMeasureProcessInterval'
    flow_poll_frequency = 'com.wsds.aiwan.uranus.cronus.model.stats.flow.impl.FlowStatsProvider aiwanFlowPollFrequency'
    netMeasurePollDelay = 'com.wsds.aiwan.uranus.gaea.service.NetMeasureManager netMeasurePollDelay'
    site_link_select_delay = 'com.wsds.aiwan.uranus.cronus.model.site.link.impl.SiteLinkServiceImpl siteLinkSelectDelay'
    site_link_filter = 'com.wsds.aiwan.uranus.gaea.model.net.netlink.impl.NetLinkServiceImpl netLinkFilter'
    pollFrequency = 'org.onosproject.provider.netconf.device.impl.NetconfDeviceProvider pollFrequency'

    @classmethod
    def get_device_flows_selector_info(cls, device_id, flows_id_list):
        commands = map(lambda x: '{} -f {} any {}'.format(cls.flows_cmd, x, device_id), flows_id_list)
        ssh_client = SshUtil(Temple.URANUS_CLI_HOST, Temple.URANUS_CLI_PORT, Temple.URANUS_CLI_USER,
                             Temple.URANUS_CLI_PASSWORD)
        ssh_client.ssh_connect()
        ret = map(lambda x: re.search(r'selector=\[(.+?)\]', x[1]).group(1), ssh_client.ssh_cmd_list(commands))
        ssh_client.ssh_close()
        return ret

    @classmethod
    def set_es_server(cls):
        commands = ['{} {}{}'.format(cls.set_cfg + cls.es_address, Temple.ES_HOST, Temple.ES_PORT)]
        ssh_client = SshUtil(Temple.URANUS_CLI_HOST, Temple.URANUS_CLI_PORT, Temple.URANUS_CLI_USER,
                             Temple.URANUS_CLI_PASSWORD)
        ssh_client.ssh_connect()
        ret = ssh_client.ssh_cmd_list(commands)
        if ret:
            assert 'is not registered' not in ret[0]
        ssh_client.ssh_close()

    @classmethod
    def set_controller_variable(cls, variable_name, t):
        commands = ['{} {}'.format(cls.set_cfg + variable_name, t)]
        ssh_client = SshUtil(Temple.URANUS_CLI_HOST, Temple.URANUS_CLI_PORT, Temple.URANUS_CLI_USER,
                             Temple.URANUS_CLI_PASSWORD)
        ssh_client.ssh_connect()
        ssh_client.ssh_cmd_list(commands)
        ssh_client.ssh_close()
