from flask import Blueprint, render_template, redirect
from dataclasses import dataclass
import requests
from oauthlib.oauth2 import WebApplicationClient
import URI

login_route = Blueprint('login',__name__)

GOOGLE_CLIENT_ID = URI.URI_GOOGLE_CLIENT_ID
GOOGLE_CLIENT_SECRET = URI.URI_GOOGLE_CLIENT_SECRET

oauth = WebApplicationClient(client_id=GOOGLE_CLIENT_ID)

@dataclass
class GoogleHosts:
    authorization_endpoint: str
    token_endpoint: str
    userinfo_endpoint: str
    certs: str

def get_google_oauth_hosts() -> GoogleHosts:
    hosts = requests.get('https://accounts.google.com/.well-known/openid-configuration')
    if hosts.status_code != 200:
        raise Exception('Não foi possível recuperar os endpoints de autenticação!')
    
    data = hosts.json()
    return GoogleHosts(authorization_endpoint=data.get('authorization_endpoint'), 
                       token_endpoint=data.get('token_endpoint'),
                       userinfo_endpoint=data.get('userinfo_endpoint'),
                       certs=data.get('jwks_uri'))

@login_route.route('/')
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