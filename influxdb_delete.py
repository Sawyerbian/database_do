from influxdb_client import InfluxDBClient
import influxdb_config
client = influxdb_config.connection()

delete_api = client.delete_api()

"""
Delete Data
"""
start = "2022-11-18T01:31:38.0750572Z"
stop = "2022-11-27T01:31:38.0750572Z"
delete_api.delete(start, stop, '_measurement="measurement1"', bucket='hot_butyl', org='battery')

"""
Close client
"""
client.close()