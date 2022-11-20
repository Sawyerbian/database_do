import influxdb_client, os, time
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS
from tqdm import tqdm
def connection():
    token = os.environ.get("INFLUXDB_TOKEN")
    org = "haizhong.bian@cn.bosch.com"
    url = "https://europe-west1-1.gcp.cloud2.influxdata.com"

    client = influxdb_client.InfluxDBClient(url=url, token=token, org=org)
    print('connection done')
    return client
    