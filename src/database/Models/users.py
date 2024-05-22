from peewee import Model, CharField, BooleanField
from flask_login import UserMixin
from database.database import db

class Users(Model, UserMixin):

    user_name = CharField()
<<<<<<< Updated upstream
    user_email = CharField()
=======
    user_email = CharField(unique=True)
>>>>>>> Stashed changes
    user_password = CharField()
    admin = BooleanField(default=False)

    @classmethod
    def get_by_email(cls, email):
        return cls.select().where(cls.user_email == email).first()

    class Meta:
        database = db