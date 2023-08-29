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
        
        memid   = request.session.get("memid")
        gid     = request.session.get("gid")
        
        count   = MdFavorite.objects.filter(user_id = memid ).count()
        
        context = {}  # 밖에다 변수 선언 해 두고 append?로 데이터 집어넣어서 context 보내는게 좋음
        
        if count == 0 or None :     
            context = {
                "count"     :count,
                "memid"     : memid,
                "gid"       : gid,
                }
        else :
            pagenum = request.GET.get( "pagenum" )              
            
            if not pagenum :
                pagenum = "1"
            
            pagenum = int( pagenum )                            
            start   = (pagenum -1 ) * int( page_size )            
            end     = start + int( page_size )                      
            
            if end >count :
                end = count
            
            number      = count - ( pagenum -1) * int (page_size)            
            startpage   = pagenum //int(page_block) * int(page_block) +1  
            
            if pagenum % int(page_block) == 0 :                         
                startpage -= int(page_block)                            
            
            endpage = startpage + int(page_block) -1                   
            
            pagecount = count // int(page_size)                         
            
            if count % int(page_size) >0 :                              
                pagecount += 1                                          
            
            if endpage > pagecount :
                endpage = pagecount
            
            pages = range(startpage, endpage + 1)             
           
            fav     = MdFavorite.objects.select_related('stor').filter(user_id = memid ).order_by("-fav_reg_ts").values(
                    'fav_id', 'fav_reg_ts', 'stor__stor_id', 'stor__stor_name', 'stor__stor_addr' )[start:end]
            # print(fav)
            fav_list = dict()
            
            for f in fav :
                fav_id = f["fav_id"]
                if fav_id not in fav_list :
                    fav_list[fav_id] ={
                        "stor_id"    : f["stor__stor_id"],
                        "stor_name"  : f["stor__stor_name"],
                        "stor_addr"  : f["stor__stor_addr"],
                        "fav_reg_ts" : f["fav_reg_ts"],
                        }
            
            print(fav_list)
            # for s in store :
                # logger.debug(f's.stor.stor_id : {s.stor.stor_id}')

            context = {
                "fav_list"  : fav_list,
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

    
    
