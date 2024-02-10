import tkinter as tk
import sqlite3
import style
import models as md
from widget_generators import *
import database as dc
import helper_functions


TABLE_NAME = "passman"


class WindowIntro(tk.Toplevel):

    def __init__(self):

        dc.create_passwords_table()