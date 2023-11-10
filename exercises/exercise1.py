import pandas as pd
import sqlalchemy as sa

#source URL
source_url = "https://opendata.rhein-kreis-neuss.de/api/v2/catalog/datasets/rhein-kreis-neuss-flughafen-weltweit/exports/csv"

#Reading the data
data = pd.read_csv(source_url, sep=";", lineterminator="\n")

#SQLite connection
sqlite_conn = "sqlite:///airports.sqlite"

#SQLAlchemy engine
engine = sa.create_engine(sqlite_conn)

#Write the data in the table "airports"
data.to_sql("airports", engine, index=False, if_exists="replace")

#Confirmation message
print("Data pipeline completed successfully!")