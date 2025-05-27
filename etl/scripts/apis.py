import pandas as pd
import requests
from warehouse import DataWareHouse


class Test:
    def __init__(self, url="https://datasets-server.huggingface.co/rows?dataset=Saatarkin%2Fmovies&config=default&split=train&offset=0&length=100"):
        self.url = url
    
    def load(self):
        response = requests.get(self.url)
        data = response.json()
        df = pd.DataFrame(data)
        return df
    
    def save(self):
        data = self.load()
        dw = DataWareHouse(table_name="test_table", data=data)


class Huggingface:
    def __init__(self, uri):
        pass


