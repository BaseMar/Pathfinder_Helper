import mysql.connector
class MySQL_Service:
    def __init__(self, table):
        self.host = 'localhost'
        self.user = 'Martino'
        self.password = '12345'
        self.database = 'pathfinderschema'
        self.table = table
        self.connection = None
        self.cursor = None
        self.data = []

    def connect(self):
        self.connection = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )
        self.cursor = self.connection.cursor()

    def disconnect(self):
        if self.connection:
            self.connection.close()

    def load_data(self, data_container):
        if not self.connection:
            self.connect()

        query = f"SELECT * FROM {self.table}"
        self.cursor.execute(query)

        columns = [column[0] for column in self.cursor.description]

        for row in self.cursor.fetchall():
            row_data = dict(zip(columns, row))
            container = data_container(row_data)
            self.data.append(container)
        return self.data

    def print_data(self):
        for container in self.data:
            print(container)
