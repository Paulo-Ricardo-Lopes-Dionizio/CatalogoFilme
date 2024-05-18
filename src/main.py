from flask import Flask
from config import *

app = Flask(__name__)

configure_all(app)

app.run(debug=True)