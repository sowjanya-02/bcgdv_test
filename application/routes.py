from application.models import  watchmodel
from application.db import db
from flask import abort,request,Blueprint
import jsonify
from collections import Counter

api_namespace = Blueprint('api', __name__)


@api_namespace.route('/checkout',methods = ['GET','POST'])
def ordercheckout():
        '''
        write a query
           1) Input paramater should be query argument or payload in json
           2) frequency of watchid is calculated using counter
           3) depending on on_offer basis the price is calculated by integrating discount price
        '''
        args = request.get_json()
        if not args: query_par = request.args.get('ids').split(',')
        if args: query_par = args['ids']
        repeated_frequency = dict(Counter(query_par))
        total_price = 0
        for watchid,quantity in repeated_frequency.items():
             query_watches = watchmodel.objects.get(watchid=watchid)
             discount_query = query_watches.discount
             if query_watches['on_offer'] == True:
                 total_price += (int(quantity / discount_query['discount_maxquantity']) * discount_query['discount_offer']) + ((quantity % discount_query['discount_maxquantity']) * query_watches['price'])
                
             else:
                 total_price  += quantity * query_watches['price']
                               
        result = {'total_price':total_price}
        
        return result