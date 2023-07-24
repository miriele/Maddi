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
        # logger.debug(f'count : {count}')
        
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
            "store" : store,
            "md_fav"   : md_fav,

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

    
    
# 즐겨찾기 추가용 url
################################   
# 좋아요와 같은 방식으로 해서 이상한 ajax로 동작은 할 것임
# 검색이랑 매장이랑 연결되고 매장눌러서 들어갈수 있게 되면 연결할 예정
#################################
class AddFavView( View ):
    @method_decorator( csrf_exempt )
    def dispatch(self, request, *args, **kwargs):
        return View.dispatch(self, request, *args, **kwargs)
    
    def get (self, request):
        template = loader.get_template( "md_favorite/addfav.html" )
        memid    = request.session.get("memid")
        gid      = request.session.get("gid")
        
        logger.debug(f'memid : {memid}')
        
        ###### 값 박아 놓음 #######
        stor_id = 7
        pagenum = 1
        number  = 1
        
        result = 0
        md_fav = MdFavorite.objects.filter(stor = stor_id)
        
        for fav in md_fav :
            logger.debug(f'fav.user_id : {fav.user_id}')
            if fav.user_id == memid :
                result = 1
                break

        logger.debug(f'result : {result}')
        
        context = {
            "result"  : result,
            "stor_id" : stor_id,
            "pagenum" : pagenum,
            "number"  : number,
            }
        return HttpResponse(template.render(context, request ) )
        
    def post(self, request ):
        memid = request.session.get("memid")
        gid   = request.session.get("gid")
        
        stor_id = request.POST.get("stor_id","")    #7
        pagenum = request.POST.get("pagenum","")    #1
        number  = request.POST.get("number","")     #1
        
        logger.debug(f'stor_id : {stor_id}')
        logger.debug(f'pagenum : {pagenum}')
        logger.debug(f'number  : {number}')
        
        favo = MdFavorite.objects.filter( user = memid, stor = stor_id ).count()
        logger.debug(f'favo : {favo}')
        
        result = 0
        
        if favo == 0 :
            favo = MdFavorite(
                user_id    = memid,
                stor_id    = stor_id,
                fav_reg_ts = datetime.now()
                )
            favo.save()
            result = 1
        else :
            favo = MdFavorite.objects.filter( user = memid, stor = stor_id )
            favo.delete()
            result = 0
            
        logger.debug(f'result : {result}')

        return HttpResponse(result)
