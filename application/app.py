from flask import Flask
from flask_restplus import Api


def create_app():
    from application.routes import api_namespace
    

    app = Flask(__name__)
    
    from application.db import initialize_db
    app.config['MONGODB_SETTINGS'] = {
      'host': 'mongodb://localhost:27017/watchmodel'
    }
    initialize_db(app)

    #api.add_namespace(api_namespace)
    app.register_blueprint(api_namespace)

    return app