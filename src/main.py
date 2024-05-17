from flask import Flask, render_template
from flask_wtf.csrf import CSRFProtect
from config import *

app = Flask(__name__)
csrf = CSRFProtect

configure_all(app)

app.run(debug=True, ssl_context='adhoc')