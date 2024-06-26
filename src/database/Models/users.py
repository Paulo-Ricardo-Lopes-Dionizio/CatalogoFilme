from peewee import Model, CharField, BooleanField
from flask_login import UserMixin
from database.database import db

class Users(Model, UserMixin):

    user_name = CharField()
    user_email = CharField(unique=True)
    user_password = CharField()
    admin = BooleanField(default=False)

    @classmethod
    def get_by_email(cls, email):
        return cls.select().where(cls.user_email == email).first()

    class Meta:
        database = db