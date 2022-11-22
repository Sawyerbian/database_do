import influxdb_client, os, time
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS
import influxdb_config
client = influxdb_config.connection()

bucket="hot_butyl"

write_api = client.write_api(write_options=SYNCHRONOUS)
   
for value in np.random.random(10):
  value = value.astype(int)
  for location in ['beijing','shanghai','tianjin']:
    point = (
      Point("measurement1")
      .tag("location", location)
      .field("temperature", value)
    )
    write_api.write(bucket=bucket, org="battery", record=point)
    #time.sleep(1) # separate points by 1 second

print(f'write is done')