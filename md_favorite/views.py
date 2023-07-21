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

# 즐겨찾기 목록 보기
page_size = 20
page_block = 3
class FavoriteView( View ):
    def get(self, request ):
        
        template = loader.get_template( "md_favorite/favorite.html" )
        '''
        count = MdComb.objects.all().count()
        if count == 0 :     #30
            context = {
                "count" :count,
                }
        else :
            pagenum = request.GET.get( "pagenum" )              #5
            if not pagenum :
                pagenum = "1"
            pagenum = int( pagenum )                            #5
            start = (pagenum -1 ) * int( page_size )            #4*5=    20
            end = start + int( page_size )                      #20+5=    25
            if end >count :
                end = count
            # md_comb = MdComb.objects.order_by("-comb_id")[start:end]
            number = count - ( pagenum -1) * int (page_size)            #30-4*5=30-20=    10
            
            startpage = pagenum //int(page_block) * int(page_block) +1  # = 5//3*3+1=1*3=3+1= 4
            if pagenum % int(page_block) == 0 :                         #5%3==0>1.666!=0
                startpage -= int(page_block)                            #  4-3 ==     1
            endpage = startpage + int(page_block) -1                    # = 4(1) +3 -1 > 6or 3
            
            pagecount = count // int(page_size)                         #  30//5=    6
            if count % int(page_size) >0 :                              #30%5나머지=0 0보다 크면
                pagecount += 1                                          #카운트가 31이어서 나머지 생기면 페이지 추가해줘야 하니 +1 더해 값 넣겠
            if endpage > pagecount :
                endpage = pagecount
            pages = range(startpage, endpage + 1)             
            '''
        context = {
         
            }
        return HttpResponse(template.render(context, request ) )

    
    
# 혹시 모를 즐겨찾기 추가용 url
class AddFavView( View ):
    def get(self, request ):
        template = loader.get_template( "md_favorite/addfav.html" )
        context = {
            }
        return HttpResponse(template.render( context, request ) )
         