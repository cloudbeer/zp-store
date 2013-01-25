zp-store
=========================

******
Notice: This project is not accomplished. Cloudbeer is a python newbie.

这个项目还没有完成，请谨慎下载，并且作者是 python 初学者
******


### An online light shop with python, web.py. Database is mongodb now.
-----------------------------


Depends on:

* [zp-db-mongo](https://github.com/cloudbeer/zp-db-mongo "zp-db-mongo")
* [web.py](http://webpy.org/ "web.py")
* [mongodb](http://www.mongodb.org/) (can change later with zp-db-?)
* [baidu ueditor](http://ueditor.baidu.com/website/)
* [bootstrap](http://twitter.github.com/bootstrap/index.html)
* [Mako](http://www.makotemplates.org/)


My nginx with uWSGI config:


    server {
        listen  80;
        server_name     zp-store;
        location / {
                include uwsgi_params;
                uwsgi_pass 127.0.0.1:9090;
         }
        location /favicon.ico {
                alias /home/cloudbeer/projects/zp-store/favicon.ico;
        }
        location /upload {
                alias /home/cloudbeer/projects/zp-store/upload;
        }
    }


Start uWSGI with (at app folder):
    uwsgi -s :9090 -w index
