"""
WSGI config for imglst project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

# 2018-03-02 13:20:00  00000001

import os

from django.core.wsgi import get_wsgi_application

os.environ["S_TYPE"] =  "REAL"
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "imglst.settings")

application = get_wsgi_application()
