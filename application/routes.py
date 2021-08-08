import http.client
from datetime import datetime
from typing import List
from flask_restplus import Namespace, Resource, fields
from application.models import discount, watchmodel
from application.db import db
from flask import abort,request,Blueprint
import jsonify
from collections import Counter

api_namespace = Blueprint('api', __name__)


@api_namespace.route('/checkout',methods = ['GET','POST'])
def ordercheckout():
    if request.method == 'GET':
        '''
        Retrieves all the watches
        '''
        #watches = watchmodel.objects().to_json()
        #return watches

    #if request.method == 'POST':
        '''
        write a query
        '''
        args = request.get_json()
        repeated_frequency = dict(Counter(args['ids']))
        watchids = list(repeated_frequency.keys())
        num_items = list(repeated_frequency.values())
        total_price = 0
        for watchid,quantity in repeated_frequency.items():
             query_watches = watchmodel.objects.get(watchid=watchid)
             discount_query = query_watches.discount
             if query_watches['on_offer'] == True:
                 total_price += (int(quantity / discount_query['discount_maxquantity']) * discount_query['discount_offer']) + ((quantity % discount_query['discount_maxquantity']) * query_watches['price'])
                
             else:
                 total_price  += quantity * query_watches['price']
                               


        #print (query_watches.to_json())
        result = {'total_price':total_price}
        
        return result, http.client.CREATED