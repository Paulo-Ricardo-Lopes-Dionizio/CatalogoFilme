from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required
from database.Models.users import Users
from werkzeug.security import generate_password_hash

user_route = Blueprint('user', __name__)

"""

##    ROTAS USUÁRIOS    ##

/user/ (GET) -- lista os usuários
/user/ (POST) -- inserir um novo usuário no banco de dados
/user/new/ (GET) -- exibe um formulario para a criação de um novo usuário
/users/<int:id> (GET) -- exibe dados de um usuário em específico
/users/<int:id>/edit/ (GET) -- exibe um formulário com os dados do usuário selecionado para editar
/users/<int:id>/update/ (PUT) -- envia uma atualização do usuário para o servidor
/users/<int:id>/delete/ (DELETE) -- deleta o usuário escolhido do servidor

"""

@user_route.route('/')
@login_required
def list_users():
    users = Users.select()

    return render_template('users/list.html', users=users)


@user_route.route('/', methods=['POST'])
def insert_users():

    name = request.form['name']
    email = request.form['email']
    password = generate_password_hash(request.form['password'])
    new_user = Users.create(user_name=name, user_email=email, user_password=password)

    return redirect(url_for('login.login_form'))


@user_route.route('/new')
def form_new_users():
 
    return render_template('users/new.html')


@user_route.route('/<int:user_id>')
@login_required
def show_user(user_id):

    user = Users.get_by_id(user_id)

    return render_template('users/show.html', user=user)


@user_route.route('/<int:user_id>/edit')
@login_required
def form_edit_user(user_id):

    user = Users.get_by_id(user_id)

    return render_template('users/edit.html', user=user)


@user_route.route('/<int:user_id>/update', methods=['PUT'])
@login_required
def update_user(user_id):

    user = Users.get_by_id(user_id)
    user.user_name = request.form['name']
    user.user_email = request.form['email']
    user.user_password = request.form['password']
    user.save()

    return redirect(url_for('user.show_user', user_id=user_id))


@user_route.route('/<int:user_id>/delete', methods=['POST','DELETE'])
@login_required
def delete_user(user_id):

    user = Users.get_by_id(user_id)
    user.delete_instance()
    return redirect(url_for('user.list_users'))