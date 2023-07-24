from django.shortcuts import render
from django.template import loader
from django.views.generic.base import View
from django.http.response import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from datetime import datetime
import logging
from md_review.models import MdReview

# 로그
logger = logging.getLogger( __name__ )


# 리뷰 보기 폼>매뉴 정보페이지에 합체
class ReviewView( View ):
    def get(self, request ):
        template = loader.get_template( "md_review/review.html" )   ########
        
        stor_id = request.GET["stor_id"]
        stor_id = int(stor_id)######
        
        count = MdReview.objects.filter('''stor_id = stor_id''').count()
        
        if count == 0 :     
            context = {
                "count" :count,
                }
        else :
            rev_ord = MdReview.objects.select_related('ordr')
            
            
            
            context = {
                "count" :count,
                }
        return HttpResponse(template.render( context, request ) )
    
    
    
    
    
    
    
    
    
# 리뷰 작성 폼
class RevwriteView( View ):
    def get(self, request ):
        template = loader.get_template( "md_review/revwrite.html" )
        context = {
            }
        return HttpResponse(template.render( context, request ) )
    