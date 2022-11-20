import influxdb_client, os, time
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS
import influxdb
client = influxdb.connection()
bucket="test"

write_api = client.write_api(write_options=SYNCHRONOUS)
   
for value in range(5):
  point = (
    Point("measurement1")
    .tag("tagname1", "tagvalue1")
    .field("field1", value)
  )
  write_api.write(bucket=bucket, org="haizhong.bian@cn.bosch.com", record=point)
  time.sleep(1) # separate points by 1 second

print(f'write in done')