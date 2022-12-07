"""
for influxdb v1:
"""
"""import influxdb_client, os, time
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS
from tqdm import tqdm
def connection():
    #token = os.environ.get("INFLUXDB_TOKEN")
    token = 'v-k-YeEWpI0-UJVI666LLMPLTLqDvgpDBnlKO_0w9DW0uEQlNMdngegO_kV_TtFCwtH9uYKlTYw1EBj0EWCl1Q=='
    org = "battery"
    #url = "https://us-west-2-1.aws.cloud2.influxdata.com/"

    #client = InfluxDBClient(url="http://localhost:8088",token=token, org=org)
    client = InfluxDBClient(url="10.179.120.240:8086", username="admin", password="123456")  # for influxdb V1
    print('connection done')
    return client

if __name__ == "__main__":
    connection()"""

from influxdb import InfluxDBClient
from datetime import datetime as dt



def connection():

    host='10.179.120.240'
    port=8086
    database="st214"

    client = InfluxDBClient(host=host, port=port,database=database)  # for influxdb V1
    print('connection done')
    return client

if __name__ == "__main__":
    connection()