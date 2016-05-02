#!/usr/bin/python

'''
GetOrders of a buyer via eBay Trading API
used to receive the approximate arrival dates of ordered items
Script by: Ilya Holtz
'''

from ebaysdk.exception import ConnectionError
from ebaysdk.trading import Connection as Trading
import datetime

# Define Section  #############################################################

sellerName = "dealsbuy2015"
myAuthToken = ""
myAppID = ""
myDevID = ""
myCertID = ""
myFlags = {'CreateTimeFrom': datetime.datetime(2016, 4, 1, 11, 17, 4),
		   'CreateTimeTo': datetime.datetime(2016, 4, 25, 11, 17, 4),
		   'ListingType' : 'Half',
		   'OrderRole' : 'Buyer',
		   'OrderStatus' : 'Shipped',
	    	'DetailLevel': 'ReturnAll',
	    	'Pagination': {
	    		'EntriesPerPage': '200',
	    		'PageNumber': '1'
	 			} 
    		}

################################################################ Define Section

try:    
    api = Trading(config_file=None, appid=myAppID, devid=myDevID, certid=myCertID, token=myAuthToken)
    response = api.execute('GetOrders',myFlags)
    # fbArray = response.reply.FeedbackDetailArray.FeedbackDetail
    # for fbDetail in fbArray:
    print response.reply
except ConnectionError as e:
    print(e)
    print(e.response.dict())
