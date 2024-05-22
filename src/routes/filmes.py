from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required
from database.Models.filmes import Filmes
from auth_jwt import token_verify

filme_route = Blueprint('filmes', __name__)

"""

##    ROTAS FILMES    ##

/filmes/ (GET) -- lista os filmes
/filmes/ (POST) -- inserir filmes no servidor
/filmes/new/ (GET) -- exibe um formulario para a adição de um novo filme
/filmes/<int:id> (GET) -- exibe dados de um filme em específico
/filmes/<int:id>/edit/ (GET) -- exibe um formulário com os dados do cliente selecionado para editar
/filmes/<int:id>/update/ (PUT) -- envia uma atualização do cliente para o servidor
/filmes/<int:id>/delete/ (DELETE) -- deleta o usuário escolhido do servidor


"""

#rota principal de filmes
@filme_route.route('/')
@login_required
def index():

    return render_template('index_filmes.html')

@filme_route.route('/IA')
def Ia():

    return render_template('IA.html')

#rota para listar os filmes
@filme_route.route('/listar', methods=['GET','POST','PUT','DELETE'])
@login_required
def listar_filmes():

    filmes = Filmes.select()

    return render_template('listar_filmes.html', filmes = filmes)


#rota para inserir um novo filme no banco de dados    
@filme_route.route('/inserir', methods=['POST'])
@login_required
def inserir_filmes():
    data = request.json
    Filmes.create(
        filme_nome = data['nome'],
        filme_data = data['data'],
        filme_genero = data['genero'],
        filme_duracao = data['duracao'],
        filme_sinopse = data['sinopse'],
        #filme_poster = data['poster'],
        )
    return redirect(url_for('filmes.listar_filmes'))


#rota para apresentar o formulário de criação de um novo filme 
@filme_route.route("/new")
@login_required
def form_create_filme():
    return render_template('form_filme.html')


#rota para apresentar os dados do filme escolhido
@filme_route.route("/<int:filme_id>")
@login_required
def dados_filme():
    return render_template("dados_filme.html")


#rota para apresentar o formulário de edição do filme escolhido
@filme_route.route("/<int:filme_id>/edit")
@login_required
def form_editar_filme(filme_id):

    filme = Filmes.get_by_id(filme_id)

    return render_template("form_filme.html", filme=filme)


#rota para enviar e atualizar os dados no banco de dados
@filme_route.route("/<int:filme_id>/update", methods=['PUT'])
@login_required
def update_filme(filme_id):

    data = request.json

    atualiza_filme = Filmes.get_by_id(filme_id)
    atualiza_filme.filme_nome = data['nome']
    atualiza_filme.filme_data = data['data']
    atualiza_filme.filme_genero = data['genero']
    atualiza_filme.filme_duracao = data['duracao']
    atualiza_filme.filme_sinopse = data['sinopse']
    #atualiza_filme.filme_poster = data['poster']
    atualiza_filme.save()

    return redirect(url_for('filmes.listar_filmes'))


#rota para deletar o filme escolhido
@filme_route.route("/<int:filme_id>/delete", methods=['DELETE'])
@login_required
def delete_filme(filme_id):
    filme = Filmes.get_by_id(filme_id)
    filme.delete_instance()
    return {"delete": 'ok'}
