import os
import pandas as pd
import sqlite3
import urllib.request
from zipfile import ZipFile

# ---------- Downloading Zip ----------
url = 'https://gtfs.rhoenenergie-bus.de/GTFS.zip'
path = 'data/GTFS.zip'
urllib.request.urlretrieve(url, path)

# ---------- Extracting ---------- 
with ZipFile(path, 'r') as zip_ref:
        with zip_ref.open('stops.txt') as stops:

# ---------- Reading ----------
                stopsDf = pd.read_csv(stops)

# ---------- Filtering for 2001 ----------
cols = ['stop_id', 'stop_name', 'stop_lat', 'stop_lon', 'zone_id']

# ---------- Selecting Required Columns ----------
stopsData = stopsDf[stopsDf['zone_id'] == 2001][cols]

# ---------- Latitude and Longitude Validation ----------
stopsData = stopsData[(stopsData['stop_lat'].between(-90, 90)) & 
                        (stopsData['stop_lon'].between(-90, 90))]

# ---------- Missing/Invalid Data Removal ----------
stopsData.dropna(inplace=True)

# ---------- SQL DB Connection ----------
db_path = 'gtfs.sqlite'
conn = sqlite3.connect(db_path)

# ---------- Writing to the SQL DB ----------
stopsData.to_sql('stops', conn, if_exists='replace', index=False, dtype={
        'stop_id': 'Integer',
        'stop_name': 'String',
        'stop_lat': 'Float',
        'stop_lon': 'Float',
        'zone_id': 'Integer'
})

conn.close()
os.remove(path)
