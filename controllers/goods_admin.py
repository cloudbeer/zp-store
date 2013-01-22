# coding: utf-8
from zero import *
from config import page_admin
from bson.objectid import ObjectId
from entity import goods
from zippydb.mongo import *

#table = mongo_store.goods

class index(admin_controller):
    def GET(self):
        xinput = web.input(size=10, page=1)
        size = int(xinput.size)
        page = int(xinput.page)
        size = size if size > 0 else 10
        page = page if page > 0 else 1
        
        goods_list = find(goods, size=size, page=page)

        return page_admin.goods_list(goods_list)

class edit(admin_controller):
    def GET(self, name = None):
        doc = None
        if (name is not None):
            doc = find_one(goods, _id = name)
        return page_admin.goods_edit(doc)

    def POST(self, name = None):
        input = web.input()
        thegoods = goods()
        thegoods.bind(input)
        #return thegoods.dump()
        if (name is None):
            insert(thegoods)
            
        else:
            thegoods._id.val(name)
            update(thegoods)
        raise web.seeother("/admin/goods/")

class delete(admin_controller):
    def POST(self):
        _id = web.input()._id
        table.remove({"_id": ObjectId(_id)})
        return 1

    
class detail(admin_controller):
    def GET(self, path):
        return "goods", path