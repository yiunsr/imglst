#-*- coding: utf-8 -*-
from django.conf.urls import  url
from . import views 

urlpatterns = [
    url(r'^sample/?$',  views.sample),
    url(r'^landmark/?$',  views.landmark),
    url(r'^morhping/?$',  views.morhping),
    #url(r'^imagemosaic/?$',  views.mosaic),
    #url(r'^imagemorphing/?$',  views.imageorphing),
]