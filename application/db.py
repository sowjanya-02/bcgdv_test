from flask_mongoengine import MongoEngine
#from pymongo import MongoClient
db = MongoEngine()
def initialize_db(app):
    db.init_app(app)