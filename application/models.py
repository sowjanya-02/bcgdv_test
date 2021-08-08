#from typing_extensions import Required
from application.db import db

class discount(db.EmbeddedDocument):
    discount_offer = db.FloatField()
    discount_maxquantity = db.FloatField()

class watchmodel(db.Document):
    watchid = db.StringField(unique=True)
    watchname = db.StringField(required=True)
    price = db.FloatField()
    on_offer = db.BooleanField()
    discount = db.EmbeddedDocumentField(discount)
    #username = db.column(db.String)

    
