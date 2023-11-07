import pandas as pd
import pymysql
from sqlalchemy import create_engine

data = pd.read_csv("movies1.csv")
engine = create_engine('mysql+pymysql:///movies')
data.to_sql(name='movies', con=engine, if_exists='replace', index=False)
