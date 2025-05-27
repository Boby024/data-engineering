from warehouse import DataWareHouse

class PostgresSQL:
    def __init__(self, uri: str, table_name: str):
        pass

    def load(self):
        return None

    def save(self):
        data = self.load()
        dw = DataWareHouse(table_name="test_table", data=data)
