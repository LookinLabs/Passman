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

        pass