from flask import Flask, render_template, request, redirect, url_for
from flask_oauthlib.client import OAuth

app = Flask(__name__)

# Google OAuth settings
GOOGLE_CLIENT_ID = 'your_client_id_here'
GOOGLE_CLIENT_SECRET = 'your_client_secret_here'
GOOGLE_AUTH_URL = 'https://accounts.google.com/o/oauth2/auth'
GOOGLE_TOKEN_URL = 'https://accounts.google.com/o/oauth2/token'

oauth = OAuth(app)
google = oauth.remote_app(
    'google',
    consumer_key=GOOGLE_CLIENT_ID,
    consumer_secret=GOOGLE_CLIENT_SECRET,
    request_token_params={
        'scope': 'email profile'
    },
    base_url=GOOGLE_AUTH_URL,
    request_token_url=None,
    access_token_url=GOOGLE_TOKEN_URL,
    access_token_method='POST'
)

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']
    # Validate email and password here
    # ...
    return redirect(url_for('index'))

@app.route('/create_user', methods=['POST'])
def create_user():
    email = request.form['email']
    password = request.form['password']
    # Create a new user here
    # ...
    return redirect(url_for('index'))

@app.route('/login_with_google')
def login_with_google():
    return google.authorize(callback=url_for('authorized', _external=True))

@app.route('/authorized')
def authorized():
    resp = google.authorized_response()
    if resp is None:
        return 'Access denied'
    session['google_token'] = (resp['access_token'], '')
    # Get user info from Google here
    # ...
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)