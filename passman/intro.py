import tkinter as tk
import sqlite3
import style
from widget_generators import *
from database import DatabaseConnection
from pysqlitecypher import sqlitewrapper
import helper_functions


TABLE_NAME = "passman"


class WindowWelcome(tk.Toplevel):

    def __init__(self):


        self.db = sqlitewrapper.SqliteCipher(
            dataBasePath="passman.db",
            checkSameThread=False, 
            password=None
        )

        self.db.createTable(TABLE_NAME,
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
        
        self.db.insertIntoTable(TABLE_NAME ,
                                [
                                    ["hh.ee", "haha", "12345678", "this password's description"],
                                    ["asdfg.com", "asdfg", "123412", "other description"]
                                ] ,
                                commit=True
        )

        self.db.getDataFromTable(TABLE_NAME, raiseConversionError=False, omitID=False)

        # change raiseError to the True in the future
        self.db.deleteDataInTable(TABLE_NAME , 5 , commit = True, raiseError = False, updateId=True)


        self.db.updateIDs(tableName , commit = True)


        self.db.updateInTable(tableName , iDValue , colName , colValue , commit = True , raiseError = True)