import pandas as pd
import time

df = pd.read_csv('wether_data.csv')

try:
    
    df['clock'] = df['clock'].str.split(':').str[0]
    date = pd.to_numeric(df['clock'], errors='coerce')
    
    #wether statistics by countries/contient
    c_temp = df.groupby(['continent','country'])['temperature'].mean()
    c_press = df.groupby(['continent','country'])['pressure'].mean()
    c_hum = df.groupby(['continent','country'])['humidity'].mean()
    c_speed = df.groupby(['continent','country'])['speed'].mean()
    c_data = pd.DataFrame({'temp':c_temp,'pressure':c_press,'humidity':c_hum,'speed':c_speed}).reset_index()
    c_data.to_csv("wether_region.csv")

    #wether statistics by time ['clock','country']
    t_temp = df.groupby(['clock','continent'])['temperature'].mean()
    t_press = df.groupby(['clock','continent'])['pressure'].mean()
    t_hum = df.groupby(['clock','continent'])['humidity'].mean()
    t_speed = df.groupby(['clock','continent'])['speed'].mean()
    t_data = pd.DataFrame({'temp':t_temp,'pressure':t_press,'humidity':t_hum,'speed':t_speed}).reset_index()
    t_data.to_csv('wether_time.csv')
    
except Exception  as e:
    print(f"error:{e}")