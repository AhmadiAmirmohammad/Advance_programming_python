#only show the essential interface and Hide complex implementation details
from abc import ABC, abstractmethod

class DatabaseConnector(ABC):
    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def execute_query(self, query):
        pass

    def run(self, query):
        #  (Template Method Pattern)
        self.connect()
        return self.execute_query(query)


class MySQLConnector(DatabaseConnector):
    def connect(self):
        print("connecting mysql")

    def execute_query(self, query):
        return f"resualt for query: {query}"


class PostgresConnector(DatabaseConnector):
    def connect(self):
        print("connecting PostgreSQL...")

    def execute_query(self, query):
        return f"resualt query for PostgreSQL : {query}"

db = MySQLConnector()
print(db.run("SELECT * FROM users"))