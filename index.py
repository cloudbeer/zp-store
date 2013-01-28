from config import app
import sys
sys.path.append('/home/cloudbeer/projects/zp-db-mongo')


#run directly
if 0:
    if __name__ == '__main__':
        app.run()


#run uwsgi in nginx
application = app.wsgifunc()
#app.run()