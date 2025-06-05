from sqlalchemy import create_engine
from dotenv import load_dotenv
import os
import pandas as pd

load_dotenv()

class DataWareHouse:
    def __init__(self, table_name: str, data, to_append=False):
        self.table_name = table_name
        self.engine = create_engine(SQLALCHEMY_DATABASE_URI = os.getenv('DE_ETL_WAREHOUSE'))  # change this to your database URI
        self.to_append = to_append

    def save(self, df: pd.DataFrame):
        # logic to save into data warehouse
        if self.to_append:
            df.to_sql(self.table_name, con=self.engine, if_exists='append', index=False)
        else:
            df.to_sql(self.table_name, con=self.engine, if_exists='replace', index=False)