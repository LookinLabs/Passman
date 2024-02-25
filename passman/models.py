from peewee import *
from datetime import datetime


db = SqliteDatabase("passman.db")


class Password(Model):

    password_address = CharField()

    password_name = CharField()

    password = CharField()

    password_description = TextField()

    password_update = DateTimeField(default=datetime.now())


    class Meta:

        database = db
