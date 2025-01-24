from flask import Flask
from flask_mysqldb import MySQL

# Initialize the MySQL instance
mysql = MySQL()

def create_app():
    """
    Creates and configures the Flask application.

    This function initializes the Flask app, configures it, and sets up the database connection
    and routes.

    Returns:
        app: The configured Flask application instance.
    """
    # Create a Flask app instance
    app = Flask(__name__, static_folder='static', template_folder='templates')

    # Load configuration settings from a separate configuration file
    app.config.from_pyfile("../config.py")

    # Initialize the MySQL extension with the Flask app
    mysql.init_app(app)

    # Import and initialize routes for the app
    from .routes import initialize_routes
    initialize_routes(app)

    # Return the configured Flask app instance
    return app
