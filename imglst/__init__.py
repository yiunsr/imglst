#-*- coding: utf-8 -*-
import os

SERVER_AUTO = True

if SERVER_AUTO:
    SERVER_TYPE = os.environ.get('S_TYPE')
    
if SERVER_TYPE == None or SERVER_AUTO ==False:
    SERVER_TYPE = "LOCAL"   ## AUTO, LOCAL,  STAGING,  REAL,  UNITTEST  
