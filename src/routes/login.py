from flask import Blueprint, render_template, request, redirect, url_for
from werkzeug.security import check_password_hash

from flask_login import login_user
from database.Models.users import Users

login_route = Blueprint('login',__name__)

@login_route.route('/')
def login_form():
    return render_template('login/login.html')

@login_route.route('/auth', methods=['POST'])
def login_auth():
    email = request.form['email']
    password = request.form['password']

    user = Users.get_by_email(email)

    if user and check_password_hash(user.user_password, password):
        login_user(user)
        return redirect(url_for('filmes.index'))

    return 'dados invalidos'