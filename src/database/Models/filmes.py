from peewee import Model, CharField 
from database.database import db

class Filmes(Model):

    filme_nome = CharField()
    filme_data = CharField()
    filme_genero = CharField()
    filme_duracao = CharField()
    filme_sinopse = CharField()
    #filme_poster = CharField()

    class Meta:
        database = db