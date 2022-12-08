"""
for influxdb v1"""
"""import influxdb_config
import pandas as pd
client = influxdb_config.connection()
query_api = client.query_api()
csv_result = query_api.query_csv('from(bucket:"hot_butyl") |> range(start: -10m)')
df = pd.DataFrame(data=csv_result)
df.columns = df.iloc[3]
df = df.iloc[4:,:]"""


import influxdb_config
import datetime
import pytz
import numpy as np
import os
import time
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm
from glob import glob
import argparse

client = influxdb_config.connection()
main_dir = '//WX4TEFAPP01/predictive_mantainance'
#pull_interval = np.int64(600) # unit: "s"

# define pull fuc:
def pull_func(start, end):
    results = client.query('SELECT * FROM "st214" WHERE time > now() - {} AND time < now() - {}'.format(start,end))
    if not len(results.raw['series']) == 0:
        df = pd.DataFrame(results.raw['series'][0]['values'],columns=results.raw['series'][0]['columns'])
        df = df.set_index(df.iloc[:,0].values).iloc[:,1:]
        df_name = df.index[0].replace(':','_').replace('.','_')
        df.to_csv(os.path.join(main_dir,"./data/{}.csv".format(df_name)),mode='a')   # save as csv
    else:
        print(f"pull emtpy")

def read_df(df_name):
    df = pd.read_csv(df_name, index_col=0)
    return df

# define a fuc to pull data by interal of pull_interval = np.int64(600) # unit: "s"

def slice_timestamp(pull_interval):
    df_list = glob(os.path.join(main_dir,'./data/*.csv'))
    df_name = sorted(df_list, key=lambda t: os.stat(t).st_mtime)[-1]   # sort file by create time
    last_df = read_df(df_name)
    last_pull_timestamp = pd.to_datetime(last_df.iloc[[-1],:].index.values[0]) # get initial last pull timestamp 
    print(f'pull data from time : {last_pull_timestamp}')
    while True:
    
        now = datetime.datetime.now(tz=pytz.utc)  + datetime.timedelta(hours=16)
        delta_to_now = (now - last_pull_timestamp).total_seconds()

        if delta_to_now < pull_interval:
            time_to_pull = np.int64(pull_interval - delta_to_now)
            pbar = tqdm(desc='countdown timer', total = time_to_pull)
            for _ in range(time_to_pull):
                time.sleep(1)
                pbar.update(1)
                #print(delta, end='/r')
            pbar.close()
            continue
        internal_start = str(np.int64(delta_to_now) + 1) + "s"   # +1 to ensure data overlaping
        internal_end = str(np.int64(delta_to_now - pull_interval)) + "s"
        pull_func(internal_start, internal_end)
        print(f'pull data from time : {last_pull_timestamp}')
        last_pull_timestamp = last_pull_timestamp - datetime.timedelta(seconds=int(-pull_interval))

def parse_args():
    """Parse the args."""
    parser = argparse.ArgumentParser(
        description='pull data from database and save as csv')
    parser.add_argument('--pull_interval', type=int, required=True,
                        default=600)
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    slice_timestamp(pull_interval=args.pull_interval)
