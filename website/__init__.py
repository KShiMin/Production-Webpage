# make website folder a python package --> can import folder 
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
    app = Flask(__name__)
    # initialise secret key for app 
    # (in production, secret key should NOT be shared & secret key can be any string)
    app.config['SECRET_KEY'] = 'asfdghjk'
    app.config['SQLALCHEMY_DATABSE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix = '/')
    app.register_blueprint(auth, url_prefix = '/')

    return app
