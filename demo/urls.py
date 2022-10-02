#-*- coding: utf-8 -*-
from django.urls import path
from . import views 

urlpatterns = [
    path(r'^sample/?$',  views.sample),
    path(r'^landmark/?$',  views.landmark),
    path(r'^morhping/?$',  views.morhping),
    #path(r'^imagemosaic/?$',  views.mosaic),
    #path(r'^imagemorphing/?$',  views.imageorphing),
]