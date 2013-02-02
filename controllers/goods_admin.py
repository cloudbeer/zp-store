# coding: utf-8
import os

from mongo import *
from controllers import *
from config import page_admin
from entity import goods, goods_picture
import datetime
from tools import upload_path, goods_image_name, resize_image
import os

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
        xinput = web.input()
        ifile = web.input(avatar={})
        filePath_a = goods_image_name()
        filePath = filePath_a[0]
        if 'avatar' in ifile:
            ifile['avatar'].file.seek(0, os.SEEK_END)
            if ifile.avatar.file.tell() > 0:
                fout = open(filePath % '_o','w') # creates the file where the uploaded file should be stored
                ifile.avatar.file.seek(0)
                fout.write(ifile.avatar.file.read()) # writes the uploaded file to the newly created file.
                fout.close() # closes the file, upload complete.

                resize_image(filePath % '_o', filePath % '_256',  256, refMode = 'both')
                resize_image(filePath % '_o', filePath % '_512',  512, refMode = 'both')
                resize_image(filePath % '_o', filePath % '_800',  800, refMode = 'both')



        thegoods = goods()
        thegoods.bind(xinput)
        thegoods.avatar_path.zval = filePath_a[1]
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

class images(admin_controller):
    def GET(self, name=None):
        if name is not None:
            doc = find_one(goods, _id = name)
            if doc is not None:
                mImages = find(goods_picture, where={'goods_id': zpid(name)}, orderby=('display_order', 1) )
                return page_admin.goods_images(zpentity = doc, zpimamges = mImages)
            else:
                raise web.InternalError("404, goods not found.")
        return page_admin.goods_images(zpentity = None, zpimamges = None)
    def POST(self, name = None):
        xinput = web.input()
        ifile = web.input(avatar={})
        filePath_a = goods_image_name()
        filePath = filePath_a[0]

        if 'avatar' in ifile:
            ifile.avatar.file.seek(0, os.SEEK_END)
            if ifile.avatar.file.tell() > 0:
                fout = open(filePath % '_o','w') # creates the file where the uploaded file should be stored
                ifile.avatar.file.seek(0)
                fout.write(ifile.avatar.file.read()) # writes the uploaded file to the newly created file.
                fout.close() # closes the file, upload complete.

                resize_image(filePath % '_o', filePath % '_256',  256, refMode = 'both')
                resize_image(filePath % '_o', filePath % '_512',  512, refMode = 'both')
                resize_image(filePath % '_o', filePath % '_800',  800, refMode = 'both')

                thepic = goods_picture()
                thepic.bind(xinput)
                thepic.path.zval = filePath_a[1]
                thepic.goods_id.zval = name
                thepic.create_date.zval = datetime.datetime.now()
                insert(thepic)
        raise web.seeother("/admin/goods/images/" + name)