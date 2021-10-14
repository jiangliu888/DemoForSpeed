import os


class RelayControlCli(object):
    relay_ip = '10.192.9.110'

    def __init__(self):
        pass

    @classmethod
    def set_relay_controller_ip(cls, relay_ip):
        cls.relay_ip = relay_ip

    @classmethod
    def power_on(cls):
        print 'wget http://{}/ecmd?pin%20set%20k8%20off'.format(cls.relay_ip)
        ret = os.system('wget http://{}/ecmd?pin%20set%20k1%20off'.format(cls.relay_ip))
        print ret

    @classmethod
    def power_off(cls):
        print 'wget http://{}/ecmd?pin%20set%20k8%20on'.format(cls.relay_ip)
        ret = os.system('wget http://{}/ecmd?pin%20set%20k1%20on'.format(cls.relay_ip))
        print ret
