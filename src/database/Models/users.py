from peewee import Model, CharField
from database.database import db

class Users(Model):

    user_name = CharField()
    user_email = CharField()
    user_password = CharField()

    class Meta:
        database = db