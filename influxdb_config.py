import influxdb_client, os, time
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS
from tqdm import tqdm
def connection():
    #token = os.environ.get("INFLUXDB_TOKEN")
    token = 'v-k-YeEWpI0-UJVI666LLMPLTLqDvgpDBnlKO_0w9DW0uEQlNMdngegO_kV_TtFCwtH9uYKlTYw1EBj0EWCl1Q=='
    org = "battery"
    #url = "https://us-west-2-1.aws.cloud2.influxdata.com/"

    client = InfluxDBClient(url="http://localhost:8088",token=token, org=org)
    print('connection done')
    return client

if __name__ == "__main__":
    connection()