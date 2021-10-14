from influxdb import InfluxDBClient


class InfluxdbUtil(object):
    def __init__(self, host_ip, port, user, password, db_name):
        self.client = InfluxDBClient(host_ip, port, user, password, db_name)

    def query(self, sql):
        print sql
        return self.client.query(sql)

    def dropMeasurement(self, measurement):
        print 'drop measurement {}'.format(measurement)
        return self.client.drop_measurement(measurement)
