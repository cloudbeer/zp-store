# coding: utf-8

from mongo import *
from controllers import *
from config import page_admin
from entity import goods_category
import datetime

class index(admin_controller):
    def GET(self):
        return 0
        cate_list = find(goods_category, orderby=('create_date', -1))
        return page_admin.goods_category(zplist = cate_list)

class edit(admin_controller):
    def GET(self, name = None):
        if name is not None:
            doc = find_one(goods_category, _id = name)
            if doc is not None: return page_admin.goods_edit(zpentity = doc)
            else: raise web.InternalError("404, goods not found.")
        else:
            return page_admin.goods_edit(zpentity = None)

    def POST(self, name = None):
        input = web.input()
        thegoods = goods_category()
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
        remove(goods_category, _id = _id)
        return 1

    
class detail(admin_controller):
    def GET(self, path):
        return "goods", path