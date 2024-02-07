import tkinter as tk
import sqlite3
import style
from widget_generators import *
from database import DatabaseConnection
from pysqlitecypher import sqlitewrapper
import helper_functions


class WindowWelcome(tk.Toplevel):

    def __init__(self):

        self.db = sqlitewrapper.SqliteCipher(
            dataBasePath="passman.db",
            checkSameThread=False, 
            password=None
        )

        self.db.createTable("passman",
                            [
                                ["password_address", "TEXT"], 
                                ["password_name", "TEXT"], 
                                ["password", "TEXT"], 
                                ["password_description", "TEXT"], 
                                ["password_update", "TEXT"]
                            ],
                            makeSecure=True,
                            commit=True
                            )
        
        self.db.insertIntoTable(tableName , insertList , commit = True)