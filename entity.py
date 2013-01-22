from zippydb.mongo import entity, field, zpid
from zippydb.fields import zpfloat, zpdatetime, zpstr

class goods(entity):
    """
    goods
    """
    __table__ = 'goods'
    def __init__(self):
        self._id = field(zpid)
        self.code = field(zpstr)
        self.title = field(zpstr)
        self.price = field(zpfloat)
        self.sell_price = field(zpfloat)
        self.sale_price = field(zpfloat)
        self.avatar_path = field(zpstr)
        self.friendly_path = field(zpstr)
        self.content = field(zpstr)
        self.spec = field(zpstr)
        
class user(entity):
    """
    user entity
    """
    __table__ = 'user'
    def __init__(self):
        self._id = field(zpid)
        self.username = field(zpstr)
        self.password = field(zpstr)
        self.salt = field(zpstr)
        self.nick = field(zpstr)
        self.avatar = field(zpstr)
        self.email = field(zpstr)
        self.tel1 = field(zpstr)
        self.tel2 = field(zpstr)
        self.last_ip =field(zpstr)
        self.last_time = field(zpdatetime)
        self.address = field(zpstr)
        self.zipcode = field(zpstr)
        self.district = field(zpstr)
        
class order(entity):
    __table__ = 'order'
    
    
class order_item(entity):
    __table__ = 'order_item'
    
class user_address(entity):
    __table__ = 'user_address'
    
        
        
        