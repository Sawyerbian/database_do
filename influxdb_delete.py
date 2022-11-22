from influxdb_client import InfluxDBClient
import influxdb_config
client = influxdb_config.connection()

delete_api = client.delete_api()

"""
Delete Data
"""
start = "1970-01-01T00:00:00Z"
stop = "now()"
delete_api.delete(start, stop, '_measurement="measurement1"', bucket='hot_butyl', org='bosch')

"""
Close client
"""
client.close()