from erlang.libs.uranus.interface.PontusInterface import PontusInterface
from erlang.libs.uranus.UranusKeyword import UranusKeyword


class PontusKeyword(object):
    def __init__(self):
        pass

    @staticmethod
    def get_pop_to_pop_running_tunnels(s_ne_id, d_ne_id):
        ret_code, tunnels = PontusInterface.get_pop_running_tunnels_from_controller(s_ne_id)
        all_tunnels = UranusKeyword.get_ne_tunnels_from_controller_with_dst_ne_id(s_ne_id, d_ne_id)
        return [val for val in tunnels if val['tunnelId'] in map(lambda x:x['tunnelId'], all_tunnels)]

    @staticmethod
    def check_running_measure_config(key, value):
        res_code, body = PontusInterface.get_measure_config()
        assert res_code == 200, '{} is not 200'.format(res_code)
        return True if(body[key] == float(value)) else False
