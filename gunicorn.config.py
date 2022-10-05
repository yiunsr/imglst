import os
import multiprocessing
PROJECT_NAME = "imglst"

workers = multiprocessing.cpu_count() * 2 + 1
bind = 'unix:/var/run/' + PROJECT_NAME + '_gunicorn.sock'
errorlog = '/var/log/gunicorn/' + PROJECT_NAME + '_error.log'
accesslog = '/var/log/gunicorn/' + PROJECT_NAME + '_access.log'
chdir=os.path.dirname(os.path.realpath(__file__))
wsgi_app = 'imglst.wsgi_real:application'
