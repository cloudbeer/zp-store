#import os, gettext


# File location directory.
#webroot = os.path.abspath(os.path.dirname(__file__))
#
## i18n directory.
#i18dir = webroot + '/i18n'
#
#gettext.install('res', i18dir, unicode=True)
#gettext.translation('res', i18dir, languages=['en-US']).install(True)
#
from entity import *
from tools import *
print(del_goods_images('/upload/2012/01/' + 'TTT%sd.jpg'))


from config import app

#run directly
#if __name__ == '__main__':
#    app.run()
#if __name__ == '__main__':
#    app.run()


import yaml

#d = {'x': 1, 'y': 2, 'a': 100}
#
#print(sbv6(d))
#
#print(yaml.dump(dict(sbv6(d)),  default_flow_style=False))