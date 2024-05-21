from flask import Blueprint, render_template, request, redirect, url_for, flash
from werkzeug.security import check_password_hash

from flask_login import login_user, login_required, logout_user
from flask_jwt_extended import create_access_token, jwt_required, JWTManager, get_jwt
from database.Models.users import Users

login_route = Blueprint('login',__name__)
jwt_manager = JWTManager()

@login_route.route('/')
def login_form():
    return render_template('login/login.html')



@login_route.route('/auth', methods=['POST'])
def login_auth():
    email = request.form['email']
    password = request.form['password']

    user = Users.get_by_email(email)

    if user and check_password_hash(user.user_password, password):
        access_token = create_access_token(identity=user.id)
        login_user(user)
        # return jsonify(access_token=access_token)
        return redirect(url_for('filmes.index'))
    
    flash('dados invalidos')
    return render_template('login/login.html')



@login_route.route('/logout')
@login_required
@jwt_required()
def logout():
    token = request.args.get('jwt')
    jwt_data = get_jwt(token)
    jti = jwt_data["jti"]
    jwt_manager.revoke_token(jti)
    logout_user()
    return redirect(url_for('login.login_form'))