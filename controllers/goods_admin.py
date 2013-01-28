# coding: utf-8

from mongo import *
from controllers import *
from config import page_admin
from bson.objectid import ObjectId
from entity import goods
import datetime

class index(admin_controller):
    def GET(self):
        xinput = web.input(size=10, page=1)
        size = int(xinput.size)
        page = int(xinput.page)
        size = size if size > 0 else 10
        page = page if page > 0 else 1
        
        goods_list = find(goods, size=size, page=page, orderby=('create_date', -1))
        return page_admin.goods_list(zplist = goods_list)

class edit(admin_controller):
    def GET(self, name = None):
        if name is not None:
            doc = find_one(goods, _id = name)
            if doc is not None: return page_admin.goods_edit(zpentity = doc)
            else: raise web.InternalError("404, goods not found.")
        else:
            return page_admin.goods_edit(zpentity = None)

    def POST(self, name = None):
        input = web.input()
        thegoods = goods()
        thegoods.bind(input)
        thegoods.update_date.zval = datetime.datetime.now()
        #return thegoods.dump()
        if name is None:
            thegoods.create_date.zval = datetime.datetime.now()
            insert(thegoods)
        else:
            thegoods._id.val(name)
            update(thegoods)
        raise web.seeother("/admin/goods/")

class delete(admin_controller):
    def POST(self):
        _id = web.input()._id
        remove(goods, _id = _id)
        return 1

    
class detail(admin_controller):
    def GET(self, path):
        return "goods", path