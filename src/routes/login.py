from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify
from werkzeug.security import check_password_hash
from datetime import timedelta
from database.Models.users import Users

from flask_login import login_user, login_required, logout_user
from flask_jwt_extended import create_access_token, JWTManager, jwt_required, get_jwt

login_route = Blueprint('login', __name__)
jwt_manager = JWTManager()

@login_route.route('/')
def login_form():
    return render_template('login/login.html')

@login_route.route('/auth', methods=['POST'])
def login_auth():
    email = request.form.get('email')
    password = request.form.get('password')

    user = Users.get_by_email(email)

    if user and check_password_hash(user.user_password, password):
        access_token = create_access_token(identity=user.id, expires_delta=timedelta(minutes=30))
        login_user(user)
        return jsonify(access_token=access_token), 200
    return jsonify({"msg": "Invalid credentials"}), 401

@login_route.route('/logout', methods=['POST'])
@login_required
@jwt_required()
def logout():
    jti = get_jwt()['jti']
    BLACKLIST.add(jti)
    logout_user()
    return jsonify(msg="Logout realizado com sucesso!"), 200

@login_route.route('/testes')
@login_required
@jwt_required()
def teste():
    jti = get_jwt()['jti']
    BLACKLIST.add(jti)
    user_id = get_jwt_identity()
    return jsonify(user_id=user_id)
