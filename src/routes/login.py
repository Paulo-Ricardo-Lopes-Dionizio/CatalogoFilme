from flask import Blueprint, render_template, request, jsonify
from werkzeug.security import check_password_hash
from database.Models.users import Users
from flask_login import login_user, login_required, logout_user
from auth_jwt import token_creator, token_verify



login_route = Blueprint('login', __name__)
@login_route.route('/')
def login_form():
    return render_template('login/login.html')

@login_route.route('/auth', methods=['POST'])
def login_auth():

    email = request.form.get('email')
    password = request.form.get('password')

    user = Users.get_by_email(email)

    if user and check_password_hash(user.user_password, password):

        token = token_creator.create(uid=user.id)

        login_user(user)
        return jsonify({'token':token}), 200
    
    return jsonify({"msg": "Invalid credentials"}), 401


@login_route.route('/logout', methods=['GET','POST'])
@login_required
@token_verify
def logout():
    logout_user()
    return jsonify(msg="Logout realizado com sucesso!"), 200