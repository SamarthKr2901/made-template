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

dtypes = {
    "column_1": sa.types.INTEGER,
    "column_2": sa.types.TEXT,
    "column_3": sa.types.TEXT,
    "column_4": sa.types.TEXT,
    "column_5": sa.types.TEXT,
    "column_6": sa.types.TEXT,
    "column_7": sa.types.REAL,
    "column_8": sa.types.REAL,
    "column_9": sa.types.INTEGER,
    "column_10": sa.types.REAL,
    "column_11": sa.types.TEXT,
    "column_12": sa.types.TEXT,
    "geo_punkt": sa.types.TEXT
}

#Write the data in the table "airports"
data.to_sql("airports", engine, index=False, if_exists="replace", dtype=dtypes)

#Confirmation message
print("Data pipeline completed successfully!")