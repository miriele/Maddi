from django.shortcuts import render, redirect
from django.template import loader
from django.views.generic.base import View
from django.http.response import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from datetime import datetime
import logging
from md_combi.models import MdComb, MdCombM, MdCLike, MdCombR
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
            # logger.debug(f'comb_like : {comb_like}')
            
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
    @method_decorator( csrf_exempt )
    def dispatch(self, request, *args, **kwargs):
        return View.dispatch(self, request, *args, **kwargs)
    def get(self, request ):
        
        template = loader.get_template( "md_combi/combwrite.html" )
        
        memid   = request.session.get("memid")
        gid     = request.session.get("gid") 
        md_menu = MdMenu.objects.all()
        nick    = MdUser.objects.get( user_id = memid )
        dsrt_t = MdDsrtT.objects.filter(dsrt_t_id__gt=-1 ).order_by("dsrt_t_id")
        drnk_t = MdDrnkT.objects.filter(drnk_t_id__gt=-1).order_by("drnk_t_id")
        # logger.debug(f'drnk_t : {drnk_t}')
        
        context = {
            "dsrt_t"    : dsrt_t,
            "drnk_t"    : drnk_t,
            "nick"      : nick,
            "md_menu"   : md_menu,
            "memid"     : memid,
            "gid"       : gid,
            }
        return HttpResponse(template.render( context, request ) )
    
    def post(self, request):
        user_id = request.session.get("memid")
        
        dto = MdComb(
            user_id = user_id,
            comb_tit = request.POST["comb_tit"],
            comb_nop = request.POST["comb_nop"],
            comb_cont = request.POST["comb_cont"],
            comb_img = request.FILES.get("comb_img", ""), 
            comb_reg_ts = datetime.now(),
            )
        dto.save()
        return redirect("/md_combi/combwrite")      ###### 태그 완료후 이동 주소 수정해야 함

    
    
# 추천글 내용 보기
class CombDView( View ):
    def get(self, request ):
        template = loader.get_template( "md_combi/combd.html" )
        
        memid   = request.session.get("memid")
        gid     = request.session.get("gid") 
        
        comb_id = request.GET["comb_id"]
        # logger.debug(f'comb_id : {comb_id}')
        
        pagenum = request.GET["pagenum"]
        number  = request.GET["number"]
        
        # 로그인한 회원 정보
        user    = MdUser.objects.get( user_id = memid )
        
        # 선택한 추천조합 정보
        
        comb    = MdComb.objects.get( comb_id = comb_id )
        logger.debug(f'comb.comb_id : {comb.comb_id}')
        # 추천글을 작성한 유저의 닉네임
        nick    = MdComb.objects.select_related('user').filter(comb_id = comb_id )
        
        # 선택한 메뉴(태그 값)
        menu    = MdCombM.objects.select_related('comb', 'menu').filter(comb_id = comb_id)
        
        # 추천수
        likeC   = MdCLike.objects.filter(comb = comb_id).count()
        
        # 댓글 갖고있는거 빼옴
        reply   = MdCombR.objects.select_related('user').filter(comb = comb_id).order_by("-c_reply_ts")
        
        # 로그인한 회원이 추천을 했나 안했나 확인용
        comb_like = MdCLike.objects.filter(user_id = memid, comb_id = comb_id )
        
        #좋아요 버튼 용 값
        if comb_like == None :
            result = 0
        else :
            result = 1
        
        context = {
            "memid"     : memid,
            "gid"       : gid,
            "pagenum"   :pagenum,
            "number"    : number,
            "comb_id"   : comb_id,
            "user"      :user,
            "comb"      : comb,
            "nick"      : nick,
            "menu"      : menu,
            "likeC"     : likeC,
            "reply"     : reply,
            "comb_like" : comb_like,
            "result"    : result,
            }
        return HttpResponse(template.render( context, request ) )
    
    def post(self, request ):
        
        memid = request.session.get("memid")
        gid = request.session.get("gid")
        
        comb_id = request.POST.get("comb_id","")
        logger.debug(f'comb_id2 : {comb_id}')
        
        pagenum = request.POST.get("pagenum","")
        logger.debug(f'pagenum : {pagenum}')
        
        number = request.POST.get("number","")
        logger.debug(f'number : {number}')
        
        c_reply_cont = request.POST.get("c_reply_cont","")
        logger.debug(f'c_reply_cont : {c_reply_cont}')
                                            
        dto = MdCombR(
            comb_id = comb_id,
            user_id = memid,
            c_reply_cont = c_reply_cont,
            c_reply_ts =  datetime.now(),
            )
        dto.save()
            
        return HttpResponse()
# 댓글용 폼
# class CombReplyView( View ):
    

# 좋아요 설정 취소
import json   
class CLikeView( View ):
    def get(self, request ):
        
        comb_id = request.POST["comb_id"]
        pagenum = request.POST["pagenum"]
        number = request.POST["number"]
        
        memid = request.session.get("memid")
        gid = request.session.get("gid")
        
        like = MdCLike.objects.get(user_id = memid, comb_id = comb_id )
        if like  == None :
            like = MdCLike(
                comb_id = comb_id,
                user_id = memid,
                like_reg_ts = datetime.now()
                )
            like.save()
        else :
            like.delete()
        
        return redirect("/md_combi/combd?comb_id=comb_id&pagenum=pagenum&number=number")  
        
        
        # return HttpResponse(result ) 
    
    
    

    

    
    
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
    
    
    
    
    
    
    
    
    
