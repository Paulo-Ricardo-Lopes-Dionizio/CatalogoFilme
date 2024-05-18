from flask import Flask, render_template
from config import *

app = Flask(__name__)

configure_all(app)

app.run(debug=True, ssl_context='adhoc')