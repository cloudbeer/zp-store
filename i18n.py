import yaml
import os
from config import lang
from tools import webroot

from operator import itemgetter

def sbv6(d,reverse=False):
    """
    Sort a dict by key

    return a new dict
    """
    return dict(sorted(d.iteritems(), key=itemgetter(1), reverse=True))


i18dir = webroot + '/i18n'
res_path = i18dir + '/' + lang
f = open(res_path+'/res.yaml')

yaml_res = yaml.load(f.read())
if yaml_res is None:
    yaml_res = dict()

class res_class():
    def __getattr__(self, name):
        if yaml_res.has_key(name):
            return yaml_res[name]
        else:
            xname = name.split('_')
            yaml_res[name] = name if len(xname)<2 else xname[1]

            yaml.dump(sbv6(yaml_res),  file(res_path+'/res.yaml', 'w'), default_flow_style=False)
            return name
    def __setattr__(self, name, value):
        yaml_res[name] = value

r = res_class()

