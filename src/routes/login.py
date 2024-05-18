from flask import Blueprint, render_template, redirect
from database.Models.users import Users
from werkzeug.security import check_password_hash

# import requests
# from oauthlib.oauth2 import WebApplicationClient
import URI

login_route = Blueprint('login',__name__)

@login_route.route('/')
def login_form():
    return render_template('login/login.html')

@login_route.route('/auth', methods=['POST'])
def login_auth():
    email = request.form['email']
    password = request.form['password']

    user = Users.select().where(Users.user_email == email)
    check_password_hash(password, user.user_password)

# GOOGLE_CLIENT_ID = URI.URI_GOOGLE_CLIENT_ID
# GOOGLE_CLIENT_SECRET = URI.URI_GOOGLE_CLIENT_SECRET

# oauth = WebApplicationClient(client_id=GOOGLE_CLIENT_ID)

# @dataclass
# class GoogleHosts:
#     authorization_endpoint: str
#     token_endpoint: str
#     userinfo_endpoint: str
#     certs: str

# def get_google_oauth_hosts() -> GoogleHosts:
#     hosts = requests.get('https://accounts.google.com/.well-known/openid-configuration')
#     if hosts.status_code != 200:
#         raise Exception('Não foi possível recuperar os endpoints de autenticação!')
    
#     data = hosts.json()
#     return GoogleHosts(authorization_endpoint=data.get('authorization_endpoint'), 
#                        token_endpoint=data.get('token_endpoint'),
#                        userinfo_endpoint=data.get('userinfo_endpoint'),
#                        certs=data.get('jwks_uri'))

# @login_route.route('/')
# def login():
#     return render_template('login/login.html')

# @login_route.route('/auth')
# def google_auth():
#     hosts = get_google_oauth_hosts()

#     redirect_uri = oauth.prepare_authorization_request(authorization_url=hosts.authorization_endpoint,
#                                                        redirect_url='https://localhost:5000/callback/',
#                                                        scope=['openid', 'email', 'profile'])

#     return redirect(location=redirect_uri[0])

# @login_route.route('/callback')
# def callback():
#     pass