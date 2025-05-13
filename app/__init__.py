import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app(config_name):
    # Set the path for the templates folder (outside of the app folder)
    template_folder_path = os.path.join(os.path.dirname(__file__), '..', 'templates')

    # Create the Flask app instance, specifying the template folder
    app = Flask(__name__, template_folder=template_folder_path)

    # Load configurations
    if config_name == 'testing':
        app.config.from_object('config.TestingConfig')
    else:
        app.config.from_object('config.DevelopmentConfig')

    # Initialize the database
    db.init_app(app)

    # Import routes or blueprints
    from . import routes
    app.register_blueprint(routes.main)

    return app
