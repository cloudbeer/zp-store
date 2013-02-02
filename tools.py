import random
import string
import hashlib
import os
import datetime
import Image


webroot = os.path.abspath(os.path.dirname(__file__))

def rdm_code(size=8, chars=string.ascii_letters + string.digits + string.punctuation):
    return ''.join(random.choice(chars) for x in range(size))

def salt():
    return rdm_code(size=16)

def challenge_code():
    return rdm_code(size=6, chars=string.digits)

def hash_pwd(pwd, salt):
    """
    :rtype : a str
    """
    hs = hashlib.sha256(salt + pwd)
    return hs.hexdigest()

def upload_path():
    nowdate = datetime.datetime.now()
    mydir = nowdate.strftime('%Y')
    mydir2 = nowdate.strftime('%m')
    rdir = webroot+'/upload/'+mydir+'/'+mydir2
    if not os.path.exists(rdir):
        os.makedirs(rdir)
    return rdir, '/upload/' + mydir + '/'+mydir2

def goods_image_name(ext='.jpg'):
    rdmName = rdm_code(6, chars=string.ascii_letters+string.digits)
    upath = upload_path()[0] + '/' + rdmName + '%s' + ext
    if not os.path.exists(upath%''):
        return upath, upload_path()[1] + '/' + rdmName + '%s' + ext
    else:
        goods_image_name(ext)

#TODO: This Method is not finished
def resize_image(file, save_path, rlen = 256, refMode='width'):
    img = Image.open(file)
    ow,oh = img.size
    mw, mh = (rlen, rlen)
    if refMode=='width': #with is 256
        mw = rlen
        mh = rlen * oh/ow
    elif refMode=='height': #let hight be 256
        mh = rlen
        mw = rlen*ow/oh
    elif refMode=='both':  #max length is 256
        if ow>oh:
            mw = rlen
            mh = rlen * oh/ow
        else:
            mh = rlen
            mw = rlen*ow/oh
#    elif refMode=='square': # resize and crop image to square
#        if (ow>oh):
#            mh = length
#            mw = length*ow/oh
#        else:
#            mw = length
#            mh = length * oh/ow


    nImg = img.resize((mw, mh), Image.ANTIALIAS)
    nImg.save(save_path)
