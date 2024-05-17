from flask import Blueprint, render_template, redirect
from dataclasses import dataclass
import requests
from oauthlib.oauth2 import WebApplicationClient
import URI

login_route = Blueprint('login',__name__)

GOOGLE_CLIENT_ID = URI.GOOGLE_CLIENT_ID
GOOGLE_CLIENT_SECRET = URI.GOOGLE_CLIENT_SECRET

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
    return render_template('login/login.html')

@login_route.route('/auth')
def google_auth():
    hosts = get_google_oauth_hosts()

    redirect_uri = oauth.prepare_authorization_request(authorization_url=hosts.authorization_endpoint,
                                                       redirect_url='https://localhost:5000/filmes/',
                                                       scope=['openid', 'email', 'profile'])

    return redirect(location=redirect_uri[0])