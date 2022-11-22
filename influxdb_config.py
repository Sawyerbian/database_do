import influxdb_client, os, time
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS
from tqdm import tqdm
def connection():
    token = os.environ.get("INFLUXDB_TOKEN")
    org = "battery"
    #url = "https://us-west-2-1.aws.cloud2.influxdata.com/"

    client = InfluxDBClient(url="http://localhost:8088",token=token, org=org)
    print('connection done')
    return client

if __name__ == "__main__":
    connection()