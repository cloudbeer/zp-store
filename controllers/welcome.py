#coding: utf-8
from controllers import *
from config import page_front
#from pymongo import MongoClient
#connection = MongoClient()

class index(controller):
    def GET(self):
        #session.user['mobile'] = '111111111'
        return page_front.index()
    
    
#class test:
#    def GET(self):
#        connection = MongoClient('localhost')
#        db = connection.local
#        coll = db.things
#        data = coll.find_one({'id':2})
#        #
#        return data #coll.find({'id':2})