import sqlite3

from src.entity.example_sqlite_enti import ExampleSqlite
from src.interface.example_repository_inte import ExampleRepositoryInterface


class SqliteRepository(ExampleRepositoryInterface):
    def __init__(self, CONN_STRIN):
        self.ng = sqlite3.connect(CONN_STRIN)

    def example(self,data):
        return "Here is example_repository for ExampleUseCase"

    def example_sqlite(self,data):
        c = self.ng.cursor()
        id=int(data['id'])
        result = []
        for row in c.execute('SELECT id, name FROM myTable where id={};'.format(id)):
            ex_obj = ExampleSqlite(id=row[0],description=row[1])
            result.append(ex_obj)
        return result