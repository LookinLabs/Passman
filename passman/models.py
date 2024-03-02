from peewee import *
from datetime import datetime
from playhouse.sqlite_ext import SqliteExtDatabase

db_key = ""

def create_passwords_table():

    db = SqliteExtDatabase("passman.db", passphrase=db_key)

    class Password(Model):

        password_address = CharField()

        password_name = CharField()

        password = CharField()

        password_description = TextField()

        password_update = DateTimeField(default=datetime.now())


        class Meta:

            database = db
