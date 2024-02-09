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


db.connect()

db.create_tables([Password])

example1 = Password.create(password_address="hh.ee", password_name="gaga", password="01234567", password_description="this password's description")

example1.save()

example2 = Password.create(password_address="asdfg.com", password_name="asdfg", password="123412", password_description="other description")

example2.save()