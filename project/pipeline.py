import os
import zipfile
import pandas as pd
import sqlalchemy as sa
from kaggle.api.kaggle_api_extended import KaggleApi

# Dataset URLs
twitch_dataset_url = 'rankirsh/evolution-of-top-games-on-twitch'
covid19_dataset_url = 'georgesaavedra/covid19-dataset'

# Get current working Directory, which is the project/pipeline.py
current_directory = os.getcwd()
# Going 1 step back and into the data folder
data_folder = os.path.join(current_directory, '..', 'data')
# Checking if the Data folder is already there, if not, creating it
if not os.path.exists(data_folder):
    os.makedirs(data_folder)

print("authenticating with Kaggle")

api = KaggleApi()
api.authenticate()

print("authenticating Successfully")

# Downloading Twitch Dataset
try:
    api.dataset_download_files(twitch_dataset_url, path=data_folder, unzip=True)
except KeyError:
    print("Error: 'Content-Length' header not found in the response from the Kaggle API for Twitch dataset.")

print("Twitch Data Downloaded")

# Downloading COVID-19 Dataset
try:
    api.dataset_download_files(covid19_dataset_url, path=data_folder, unzip=True)
except KeyError:
    print("Error: 'Content-Length' header not found in the response from the Kaggle API for COVID-19 dataset.")

print("covid data downloaded")

# Displaying Downloaded Files
files = os.listdir(data_folder)
print("Downloaded files:", files)

# Reading Twitch Dataset
csv_file_path_twitch = os.path.join(data_folder, 'Twitch_game_data.csv')
print("Reading twitch data from"+csv_file_path_twitch)
twitch_data = pd.read_csv(csv_file_path_twitch, sep=",", lineterminator="\n", encoding='cp1252')

# Reading COVID-19 Dataset
csv_file_path_covid19 = os.path.join(data_folder, 'owid-covid-data.csv')
print("Reading covid data from"+csv_file_path_covid19)
covid_data = pd.read_csv(csv_file_path_covid19, sep=",", lineterminator="\n", encoding='cp1252')

print("Completed Reading Data")

# Updating the save path for the SQLite database file to also be in the Data folder
sqlite_file_path = os.path.join(data_folder, 'data.sqlite')

# SQLite connection
sqlite_conn = f"sqlite:///{sqlite_file_path}"

# SQLAlchemy engine
engine = sa.create_engine(sqlite_conn)

print("Established Connection with SQLite")

# Write the data to the respective tables
twitch_data.to_sql("twitch_data", engine, index=False, if_exists="replace")
covid_data.to_sql("covid_data", engine, index=False, if_exists="replace")

print("Saved Data to SQLite Database")

print("Data pipeline completed successfully!")
