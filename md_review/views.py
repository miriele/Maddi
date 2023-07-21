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

# 리뷰 작성 폼
class RevwriteView( View ):
    def get(self, request ):
        template = loader.get_template( "md_review/revwrite.html" )
        context = {
            }
        return HttpResponse(template.render( context, request ) )
    
    
# 리뷰 보기 폼>매뉴 정보페이지에 합체
class ReviewView( View ):
    def get(self, request ):
        template = loader.get_template( "md_review/review.html" )
        context = {
            }
        return HttpResponse(template.render( context, request ) )