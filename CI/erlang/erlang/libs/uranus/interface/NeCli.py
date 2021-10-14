from erlang.libs.common.SshUtil import SshUtil
from erlang.libs.common import JsonUtil


class NeCli(object):
    flows_cmd = 'flows'
    netcfg_cmd = 'netconf-get-config'

    @classmethod
    def netconf_get_config(cls, device_ip, user, password, port, xpath):
        commands = ['sysrepocfg -f json -X -x {}'.format(xpath)]
        ssh_client = SshUtil(device_ip, port, user, password)
        ssh_client.ssh_connect()
        command_ret = ssh_client.ssh_cmd_list(commands)[0]
        ssh_client.ssh_close()
        if command_ret:
            ret = JsonUtil.load_json(''.join(command_ret))
            print ret
        else:
            ret = command_ret
        return ret

    @classmethod
    def netconf_del_config(cls, device_ip, user, password, port, xpath):
        commands = ['sysrepocfg -Xexport.xml -d running -m aiwan-config',
                    "awk '/<" + xpath + ">/{skip=1;} 1{if(!skip)print;} " + r"/<\/" + xpath + ">/{skip=0}' export.xml > new.xml",
                    'sysrepocfg -Inew.xml  -d running -m aiwan-config']
        ssh_client = SshUtil(device_ip, port, user, password)
        ssh_client.ssh_connect()
        command_ret = ssh_client.ssh_cmd_list(commands)[0]
        ssh_client.ssh_close()
        return command_ret[0]
