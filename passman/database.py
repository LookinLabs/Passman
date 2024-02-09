import tkinter as tk
import sqlite3


class DatabaseConnection:

    def __init__(self) -> None:
        # durectory should be C:\Users\<username>\AppData\Roaming\<directory_name>
        self.connection = sqlite3.connect("passman.db")

        self.cursor = self.connection.cursor()


    def fetch_data(self):
            
        SQL_query = "SELECT password_name, password_address FROM passman"

        try:
            self.cursor.execute("CREATE TABLE passman (id INTEGER PRIMARY KEY AUTOINCREMENT, password_address TEXT, password_name TEXT, password TEXT, password_description TEXT DEFAULT NULL, password_update DATETIME DEFAULT CURRENT_TIMESTAMP)") # How to add timestamp?

            self.connection.commit()

            for row in self.cursor.execute("SELECT * FROM passman;"):

                print(row)

        except:

            print("Such table already exists")

        db_data =  self.cursor.execute(SQL_query)

        return db_data


    def fetch_password_data(self, sql_query, password_data, description_field):

        data = self.cursor.execute(sql_query)

        fetched_data = data.fetchall()

        password_data.set(fetched_data[0][0])

        description_field.delete("1.0", tk.END)

        description_field.insert(tk.END, fetched_data[0][1])




    def __del__(self) -> None:

        self.connection.close()