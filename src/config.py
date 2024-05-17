from routes.filmes import filme_route
from routes.users import user_route
from routes.login import login_route

from database.database import db
from database.Models.filmes import Filmes
from database.Models.users import Users


def configure_all(app):
    configure_db()
    configure_routes(app)
    # configure_googleOAuth(app)

def configure_db():
    db.connect()
    db.create_tables([Filmes, Users])

def configure_routes(app):
    app.register_blueprint(filme_route,url_prefix='/filmes')
    app.register_blueprint(user_route,url_prefix='/user')
    app.register_blueprint(login_route)