from peewee import Model, CharField, BooleanField
from database.database import db

class Users(Model):

    user_name = CharField()
    user_email = CharField()
    user_password = CharField()
    is_active = BooleanField(default=True)
    
    @classmethod
    def get_by_email(cls, email):
        return cls.select().where(cls.user_email == email).first()

    class Meta:
        database = db