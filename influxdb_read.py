import influxdb_config
import pandas as pd
client = influxdb_config.connection()
query_api = client.query_api()
csv_result = query_api.query_csv('from(bucket:"hot_butyl") |> range(start: -10m)')
df = pd.DataFrame(data=csv_result)
df.columns = df.iloc[3]
df = df.iloc[4:,:]