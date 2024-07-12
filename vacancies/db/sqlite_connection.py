import json
import sqlite3


class ConnectionHandler:

    def __init__(self):
        self.read_from_config()

    def read_from_config(self):
        with open("config.json", "r") as f:
            data = json.load(f)

        self.database = data["database"]

    def do_test(self):
        mydb = sqlite3.connect(database=self.database)
        select_query = "SELECT * FROM new_vacancies"  # ORDER BY name
        cursor = mydb.cursor()
        cursor.execute(select_query)
        result = cursor.fetchall()
        for row in result:
            print(row)

    def get_connection(self):
        return sqlite3.connect(database=self.database)

    def check_connection(self) -> bool:
        try:
            mydb = sqlite3.connect(database=self.database)
            select_query = "SELECT COUNT(*) FROM new_vacancies"
            cursor = mydb.cursor()
            cursor.execute(select_query)
            result = cursor.fetchone()
            if result and result[0] > 0:
                return True
            else:
                return False
        except sqlite3.Error as error:
            print("Ошибка при подключении к SQLite", error)
            return False


# Singleton
my_connection_handler = ConnectionHandler()
