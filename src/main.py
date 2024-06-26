from flask import Flask
from flask_login import LoginManager
from config import *

app = Flask(__name__)

configure_all(app)

login_manager= LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def user_loader(user_id):
    return Users.get_by_id(user_id)

app.run(debug=True)