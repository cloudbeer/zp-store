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
    return rdir

def goods_image_name(ext='.jpg'):
    rdmName = rdm_code(6, chars=string.ascii_letters+string.digits)
    upath = upload_path() + '/' + rdmName + '%s' + ext
    if not os.path.exists(upath%''):
        return upath
    else:
        goods_image_name(ext)

#TODO: This Method is not finished
def crop_image(file, save_path, length=256, refMode='width'):
    img = Image.open(file)
    ow,oh = img.size()
    mw, mh = (length, length)
    if refMode=='width': #with is 256
        mw = length
        mh = length * ow/oh
    elif refMode=='height': #let hight be 256
        mh = length
        mw = length*oh/ow
    elif refMode=='both':  #max length is 256
        if (ow>oh):
            mw = length
            mh = length * ow/oh
        else:
            mh = length
            mw = length*oh/ow
    elif refMode=='square': # resize and crop image to square
        pass

    nImg = img.resize(mw, mh)
    nImg.save(save_path)