import pandas as pd

def csv_df(filepath):
    data = pd.read_csv(filepath)
    df = pd.DataFrame(data)
    return df

df = csv_df("WFH Data/2 MONTHS/2_month_daily_end.csv")
df['local_date'] = pd.to_datetime(df['local_date'])
df['Week'] = df['local_date'].dt.isocalendar().week
gb = df.groupby(['subject_id', 'Week'])['LOCATION_END'].count()
mean = gb.describe()['mean']

df = csv_df("WFH Data/3 MONTHS/3_month_daily_end.csv")
df['local_time'] = pd.to_datetime(df['local_time'])
df['Week'] = df['local_time'].dt.isocalendar().week
gb = df.groupby(['rsp_id', 'Week'])['LOCATION_END'].count()
mean += gb.describe()['mean']

df = csv_df("WFH Data/4 MONTHS/4_month_daily_end.csv")
df['local_time'] = pd.to_datetime(df['local_time'])
df['Week'] = df['local_time'].dt.isocalendar().week
gb = df.groupby(['rsp_id', 'Week'])['LOCATION_END'].count()
mean += gb.describe()['mean']

mean /= 3
print(mean)
