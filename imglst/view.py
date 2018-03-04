#-*- coding: utf-8 -*-
import logging
from django.http.response import HttpResponseRedirect

logger = logging.getLogger('django_log')


def main(request):
    logger.info("/main")
    return HttpResponseRedirect('/demo/landmark') # 302