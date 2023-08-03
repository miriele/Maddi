from django.shortcuts import render, redirect
from django.template import loader
from django.views.generic.base import View
from django.http.response import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from datetime import datetime
import logging
from md_favorite.models import MdFavorite
from md_store.models import MdStor
from django.template.context_processors import request

# 로그
logger = logging.getLogger( __name__ )

# 즐겨찾기 목록 보기
page_size = 20
page_block = 3
class FavoriteView( View ):
    def get(self, request ):
        
        template = loader.get_template( "md_favorite/favorite.html" )
        
        memid = request.session.get("memid")
        gid = request.session.get("gid")
        
        count = MdFavorite.objects.filter(user_id = memid ).count()
        
        context={}# 밖에다 변수 선언 해 두고 append?로 데이터 집어넣어서 context 보내는게 좋음
        
        if count == 0 or None :     #30
            context = {
                "count"     :count,
                "memid"     : memid,
                "gid"       : gid,
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
            
            md_fav = MdFavorite.objects.filter(user_id = memid ).order_by("-fav_reg_ts")[start:end]  #####
            # for fav in md_fav :
                # logger.debug(f'fav.fav_id : {fav.fav_id}')
            
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
            
            store = MdFavorite.objects.select_related('stor').order_by("-fav_reg_ts")
            # for s in store :
                # logger.debug(f's.stor.stor_id : {s.stor.stor_id}')

            context = {
                "store"     : store,
                "md_fav"    : md_fav,
                "memid"     : memid,
                "gid"       : gid,
                "count"     : count,
                "pagenum"   : pagenum,
                "number"    : number,
                "startpage" : startpage,
                "endpage"   : endpage,
                "pages"     : pages, 
                "pageblock" : page_block,
                "pagecount" : pagecount,
            }
        return HttpResponse(template.render(context, request ) )

    
    
