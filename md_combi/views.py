from django.shortcuts import render
from django.template import loader
from django.views.generic.base import View
from django.http.response import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from datetime import datetime
import logging
from md_combi.models import MdComb, MdCombM, MdCLike
from md_member.models import MdUser
from md_store.models import MdMenu, MdDrnkT, MdDsrtT
from django.db.models.aggregates import Count

# 로그
logger = logging.getLogger( __name__ )

# 추천 목록 보기
page_size = 20
page_block = 3
class CombListView( View ):
    def get(self, request ):
        
        template = loader.get_template( "md_combi/comblist.html" )
        count    = MdComb.objects.all().count()

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
            
            md_comb   = MdComb.objects.order_by("-comb_id")[start:end]
            number    = count - (pagenum -1) * int(page_size)             #30-4*5=30-20=    10
            startpage = pagenum //int(page_block) * int(page_block) +1  # = 5//3*3+1=1*3=3+1= 4
            
            if pagenum % int(page_block) == 0 :                         #5%3==0>1.666!=0
                startpage -= int(page_block)                            #  4-3 ==     1
            
            endpage   = startpage + int(page_block) -1                    # = 4(1) +3 -1 > 6or 3
            pagecount = count // int(page_size)                         #  30//5=    6
            
            if count % int(page_size) >0 :                              #30%5나머지=0 0보다 크면
                pagecount += 1                                          #카운트가 31이어서 나머지 생기면 페이지 추가해줘야 하니 +1 더해 값 넣겠
            
            if endpage > pagecount :
                endpage = pagecount
            
            pages = range(startpage, endpage + 1)                       # 페이지들은 456 까지 나온다?
            
            # 닉네임
            comblist = MdComb.objects.select_related('user')
            
            # for comb in comblist :
                # print(comb.user.user_nick) #> 닉네임 나옴
            
            # 추천수
            comb_like = [(id.comb_id, MdCLike.objects.filter(comb=id.comb_id).count()) for id in md_comb]
            logger.debug(f'comb_like : {comb_like}')
            
            # 조합 메뉴명
            comb_menu = MdCombM.objects.select_related("comb", "menu")
            # for cm in comb_menu:
            #     for mdc in md_comb:
            #         if mdc.comb_id == cm.comb.comb_id :
            #             print( cm.menu.menu_name)
                
            gid = request.session.get("gid") 
            memid = request.session.get("memid")   
            context = {
                "memid"     : memid,
                "gid"       : gid,
                "comb_menu" : comb_menu,
                "comb_like" : comb_like,
                "comblist"  : comblist,
                "count"     : count,
                "pagenum"   : pagenum,
                "md_comb"   : md_comb,
                "number"    : number,
                "startpage" : startpage,
                "endpage"   : endpage,
                "pages"     : pages, 
                "pageblock" : page_block,
                "pagecount" : pagecount,
                 
                }
        return HttpResponse(template.render(context, request ) )
    
    
    
# 추천글 작성
class CombWriteView( View ):
    def get(self, request ):
        
        template = loader.get_template( "md_combi/combwrite.html" )
        
        memid   = request.session.get("memid")
        gid     = request.session.get("gid") 
        md_menu = MdMenu.objects.all()
        nick = MdUser.objects.get( user_id = memid )
        context = {
                "nick"      : nick,
                "md_menu"   : md_menu,
                "memid"     : memid,
                "gid"       : gid,
            }
        return HttpResponse(template.render( context, request ) )
    
'''
import json    
class SelectBView(View ):
    def get(self, request):
        
        drnk_t = MdDrnkT.objects.all()      #음료분류
        print
        dsrt_t = MdDsrtT.objects.all()      # 디저트 분류
        md_menu = MdMenu.objects.all()      # 메뉴
        
        context = {
            'drnk_t': drnk_t,
            'dsrt_t': dsrt_t,
            'md_menu' : md_menu,
        }
        return render(request, 'profile_update.html', context=context)
    
'''    
    
    
    
    
    
    
    
    
    
    
    
# 추천글 내용 보기
class CombDView( View ):
    def get(self, request ):
        template = loader.get_template( "md_combi/combd.html" )
        md_comb = MdComb.objects.all()
        md_user = MdComb.objects.select_related("user")
        comb_like = MdCLike.objects.select_related("comb").all()
        context = {
                "md_comb" : md_comb,
                "md_user" : md_user,
                "comb_like" : comb_like,
            }
        return HttpResponse(template.render( context, request ) )
    
# 댓글용 폼
class CombReplyView( View ):
     def get(self, request ):
        template = loader.get_template( "md_combi/combreply.html" )
        context = {
            }
        return HttpResponse(template.render( context, request ) )

# 댓글용 ajax      
class CombReView( View ):
    def get(self, request ):
        pass
        # return HttpResponse(result ) 
    
    
    

    

    
    
    
    
    
    
    
    
    
    
    
    
