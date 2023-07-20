from django.shortcuts import render
from django.template import loader
from django.views.generic.base import View
from django.http.response import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from datetime import datetime
import logging

# 로그
logger = logging.getLogger( __name__ )

# 추천 목록 보기
class CombListView( View ):
    def get(self, request ):
        pass