from flask import Flask
from flask_wtf.csrf import CSRFProtect
from config import *

app = Flask(__name__)
csrf = CSRFProtect

@app.route('/')
def main():
    return 'teste'

configure_all(app)

app.run(debug=True)