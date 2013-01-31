#coding: utf-8
import web
from config import page_front
from controllers import controller
from entity import user
from tools import *
from mongo import *
from i18n import r


class register(controller):
    def GET(self):
        iagree = web.input().iagree if web.input().has_key('iagree') else None
        #return iagree
        if iagree == 'true':
            return page_front.register(iagree=True)
        return page_front.register(iagree=False)

    def POST(self):
        winput = web.input()
        xuser = user()
        xuser.bind(winput)
        xuser.salt.zval = salt()
        xuser.password.zval = hash_pwd(xuser.password.zval, xuser.salt.zval)
        insert(xuser)

        raise web.seeother('/account/login/')



class login(controller):
    def GET(self):
        return page_front.login(input_email='', errors = {})

    def POST(self):
        xinput = web.input()
        email = xinput.email if xinput.has_key('email') else None
        password =  xinput.password if xinput.has_key('password') else None
        if email is None or password is None: pass
        t_user = find_one(user, {'email': email})
        if t_user is None:
            return page_front.login(input_email = email, errors={'email': r.er_EmailNotFound})
        mypwd = hash_pwd(password,t_user.salt.zval)
        print(mypwd, t_user.password.zval)
        if mypwd == t_user.password.zval:
            if xinput.has_key('backto'):
                raise web.seeother(xinput.backto)
            else:
                raise web.seeother('/')
        else:
            return page_front.login(input_email = email, errors={'password': r.er_PasswordIsWrong})
