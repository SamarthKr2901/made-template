import os
import zipfile
import pandas as pd
import sqlalchemy as sa
from kaggle.api.kaggle_api_extended import KaggleApi

# Dataset URLs
twitch_dataset_url = 'rankirsh/evolution-of-top-games-on-twitch'
covid19_dataset_url = 'https://covid19.who.int/WHO-COVID-19-global-data.csv'

# Generating the data save path
# Get current working Directory, which is the project/pipeline.py
current_directory = os.getcwd()
# Going 1 step back and into the data folder
data_folder = os.path.join(current_directory, '..', 'data')
# Checking if the Data folder is already there, if not, creating it
if not os.path.exists(data_folder):
    os.makedirs(data_folder)
download_folder = data_folder

# Download Location
# download_folder = 'C:\Users\evils\Desktop\MADE Data\MADE\made-template\data'

# This uses the Kaggle.json file which is saved in my local folder - Contains the API name + key.
# Initializing Kaggle API
api = KaggleApi()
api.authenticate()

# Downloading Dataset
api.dataset_download_files(twitch_dataset_url, path=download_folder, unzip=True)

# Reading Both Datasets
csv_file_path = os.path.join(download_folder, 'Twitch_game_data.csv')
twitch_data = pd.read_csv(csv_file_path, sep=",", lineterminator="\n", encoding='cp1252')

# Displaying Downloaded Files - COVID dataset file is not downloaded/displayed but directly added to the SQLite database
files = os.listdir(download_folder)
print("Downloaded files:", files)

# Reading WHO COVID-19 Global Data
covid19_data = pd.read_csv(covid19_dataset_url)

# Updating the save path for the SQLite database file to be also in the Data folder
sqlite_file_path = os.path.join(data_folder, 'data.sqlite')

# SQLite connection
sqlite_conn = f"sqlite:///{sqlite_file_path}"

# SQLAlchemy engine
engine = sa.create_engine(sqlite_conn)

# Write the data in the table "airports"
twitch_data.to_sql("twitch_data", engine, index=False, if_exists="replace")

# Write the COVID-19 data to the table "covid19_data"
covid19_data.to_sql("covid19_data", engine, index=False, if_exists="replace")

# Confirmation message
print("Data pipeline completed successfully!")