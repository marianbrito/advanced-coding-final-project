from flask import Flask
from flask_mysqldb import MySQL

mysql = MySQL()

def create_app():
    app = Flask(__name__, static_folder='static', template_folder='templates')

    app.config.from_pyfile('../config.py')  

    mysql.init_app(app)

    from .routes import initialize_routes
    initialize_routes(app)

    return app

