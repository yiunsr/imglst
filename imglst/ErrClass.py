#-*- coding: utf-8 -*-
import json
from django.http import HttpResponse
from rest_framework.exceptions import APIException
from rest_framework.views import exception_handler

_ERR_DICT = {
     "NOERROR" : [0 , u"정상"],
     "UNKNWON_ERROR" : [10000, u"알 수 없는 에러 입니다..",],
     "ERROR_WITH_DETAIL" : [10001, u"다음과 같은 에러가 발생했습니다.  %s " ,],
     
}

class ErrClass(APIException):
    status_code = 200
    #default_detail = 'Service temporarily unavailable, try again later.'
    
    errNo = None
    errMsg = None
    
    
    def __init__(self, errCode, errDetail = None,  server_errCode = "OK",   server_errDetail = None,  status_code = 200 ):
        self.errNo = _ERR_DICT[errCode][0]
        self.errMsg = _ERR_DICT[errCode][1]
        if errDetail : 
            self.errMsg = self.errMsg % errDetail
            
        self.status_code = status_code
    
    def __str__(self):
        return json.dumps(   { "success" :  self.errNo == 0  ,  "code"  :   self.errNo, "message"  : self.errMsg   } )

        
    def msg(self):
        return self.errMsg
    
    def toDict(self):
        return   { "success" :  self.errNo == 0  ,  "code"  :   self.errNo, "message"  : self.errMsg   }
    
    def response(self):
        return HttpResponse( json.dumps(  { "success" :  self.errNo == 0  ,  "code"  :   self.errNo, "message"  : self.errMsg   }  ), content_type="application/json" , status = self.status_code )
            

