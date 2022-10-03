#-*- coding: utf-8 -*-
from django.urls import path
from . import views 

urlpatterns = [
    path('sample',  views.sample),
    path('landmark',  views.landmark),
    path('morhping',  views.morhping),
    #path(r'^imagemosaic/?$',  views.mosaic),
    #path(r'^imagemorphing/?$',  views.imageorphing),
]