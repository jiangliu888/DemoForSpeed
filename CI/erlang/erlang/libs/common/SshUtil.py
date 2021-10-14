import paramiko


class SshUtil(object):
    def __init__(self, host_ip, port, user=None, password=None):
        self.host_ip = str(host_ip)
        print(host_ip)
        self.password = str(password)
        self.user = str(user)
        self.port = int(port)
        self.ssh = paramiko.SSHClient()

    def ssh_connect(self):
        print "begin to ssh %s" % self.host_ip
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.ssh.connect(self.host_ip, self.port, self.user, self.password)

    def ssh_cmd_list(self, cmd_list):
        rtn_list = []
        try:
            for command in cmd_list:
                print "begin to process cmd: %s" % command
                stdin, stdout, stderr = self.ssh.exec_command(command)
                cmd_rtn = stdout.readlines() + stderr.readlines()
                print "cmd{} return is:{}".format(stdin, cmd_rtn)
                rtn_list.append(cmd_rtn)
        except Exception, e:
            print "ERROR : ssh_cmd_list Exception{}! {}".format(e, cmd_list)
        return rtn_list

    def ssh_close(self):
        self.ssh.close()
