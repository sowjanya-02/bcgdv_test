from flask import Flask


def create_app():
    from application.routes import api_namespace
    

    app = Flask(__name__)
    
    from application.db import initialize_db
    ## configuration for the mongodb uri
    app.config['MONGODB_SETTINGS'] = {
      'host': 'mongodb://mongodb:27017/watchmodel'
    }
    # initializing db
    initialize_db(app)

    app.register_blueprint(api_namespace)

    return app