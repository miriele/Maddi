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
        gid   = request.session.get("gid")
        memid = request.session.get("memid")
        
        logger.debug(f'memid : {memid}')

        template = loader.get_template( "md_combi/comblist.html" )
        count    = MdComb.objects.all().count()

        if count == 0 :     #30
            context = {
                "count" : count,
                "memid" : memid,
                "gid"   : gid,
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
            
            
            
            md_comb   = MdComb.objects.select_related('user').order_by('-comb_id')[start:end]
            menu_name = MdCombM.objects.select_related('menu').order_by("-comb_id")
             
            # logger.debug(f'md_comb : {md_comb}')
            for c in md_comb:
                for mn in menu_name :
                    if mn.comb_id == c.comb_id :
                        logger.debug(f' mn.menu.menu_name : { mn.menu.menu_name}')
                # logger.debug(f'c.user.user_id : {c.user.user_id}')
                # logger.debug(f'c.comb_tit : {c.comb_tit}')
            
            
            # 추천수 용
            md_comb1   = MdComb.objects.order_by("-comb_id")[start:end]
            # 추천수
            comb_like = [(id.comb_id, MdCLike.objects.filter(comb=id.comb_id).count()) for id in md_comb1]
                
            gid = request.session.get("gid") 
            memid = request.session.get("memid")   
            logger.debug(f'memid : {memid}')
            context = {
                "memid"     : memid,
                "gid"       : gid,
                "md_comb1"  : md_comb1, 
                "comb_like" : comb_like,
                "md_comb"   : md_comb,
                "menu_name" : menu_name,
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
    
    
    
# 추천글 작성
import json
class CombWriteView( View ):
    @method_decorator( csrf_exempt )
    def dispatch(self, request, *args, **kwargs):
        return View.dispatch(self, request, *args, **kwargs)
    def get(self, request ):
        
        memid   = request.session.get("memid")
        gid     = request.session.get("gid") 
            
        template = loader.get_template( "md_combi/combwrite.html" )
        nick    = MdUser.objects.get( user_id = memid )
        
        # 2번쨰 select box
        dsrt_t  = MdDsrtT.objects.filter(dsrt_t_id__gt= -1 ).order_by("dsrt_t_id")
        drnk_t  = MdDrnkT.objects.filter(drnk_t_id__gt= -1 ).order_by("drnk_t_id")
        
        dsrtIdList   = [dsrt.dsrt_t_id   for dsrt in dsrt_t]
        dsrtNameList = [dsrt.dsrt_t_name for dsrt in dsrt_t]
        drnkIdList   = [drnk.drnk_t_id   for drnk in drnk_t]
        drnkNameList = [drnk.drnk_t_name for drnk in drnk_t]
        
        # 3번째 select box    9/7개...
        dr_m0 = MdMenu.objects.filter( dsrt_t_id = -1, drnk_t_id = 0 ) 
        # logger.debug(f'dr_m0 : {dr_m0}')
        dr_m1 = MdMenu.objects.filter( dsrt_t_id = -1, drnk_t_id = 1 )
        dr_m2 = MdMenu.objects.filter( dsrt_t_id = -1, drnk_t_id = 2 )
        dr_m3 = MdMenu.objects.filter( dsrt_t_id = -1, drnk_t_id = 3 )
        dr_m4 = MdMenu.objects.filter( dsrt_t_id = -1, drnk_t_id = 4 )
        dr_m5 = MdMenu.objects.filter( dsrt_t_id = -1, drnk_t_id = 5 )
        dr_m6 = MdMenu.objects.filter( dsrt_t_id = -1, drnk_t_id = 6 )
        dr_m7 = MdMenu.objects.filter( dsrt_t_id = -1, drnk_t_id = 7 )
        dr_m8 = MdMenu.objects.filter( dsrt_t_id = -1, drnk_t_id = 8 )
        
        ds_m0 = MdMenu.objects.filter( drnk_t_id = -1 ,dsrt_t_id = 0 )   
        ds_m1 = MdMenu.objects.filter( drnk_t_id = -1 ,dsrt_t_id = 1 )
        ds_m2 = MdMenu.objects.filter( drnk_t_id = -1 ,dsrt_t_id = 2 )
        ds_m3 = MdMenu.objects.filter( drnk_t_id = -1 ,dsrt_t_id = 3 )
        ds_m4 = MdMenu.objects.filter( drnk_t_id = -1 ,dsrt_t_id = 4 )
        ds_m5 = MdMenu.objects.filter( drnk_t_id = -1 ,dsrt_t_id = 5 )
        ds_m6 = MdMenu.objects.filter( drnk_t_id = -1 ,dsrt_t_id = 6 )
        
        # drink id
        rm0IdL = [rm0.menu_id  for rm0 in dr_m0]
        rm1IdL = [rm1.menu_id  for rm1 in dr_m1]
        rm2IdL = [rm2.menu_id  for rm2 in dr_m2]
        rm3IdL = [rm3.menu_id  for rm3 in dr_m3]
        rm4IdL = [rm4.menu_id  for rm4 in dr_m4]
        rm5IdL = [rm5.menu_id  for rm5 in dr_m5]
        rm6IdL = [rm6.menu_id  for rm6 in dr_m6]
        rm7IdL = [rm7.menu_id  for rm7 in dr_m7]
        rm8IdL = [rm8.menu_id  for rm8 in dr_m8]
        
        # dessert id
        sm0IdL = [sm0.menu_id  for sm0 in ds_m0]
        sm1IdL = [sm1.menu_id  for sm1 in ds_m1]
        sm2IdL = [sm2.menu_id  for sm2 in ds_m2]
        sm3IdL = [sm3.menu_id  for sm3 in ds_m3]
        sm4IdL = [sm4.menu_id  for sm4 in ds_m4]
        sm5IdL = [sm5.menu_id  for sm5 in ds_m5]
        sm6IdL = [sm6.menu_id  for sm6 in ds_m6]
        
        # drink name
        rm0NameL = [rm0.menu_name  for rm0 in dr_m0]
        # logger.debug(f'rm0NList : {rm0NList}')
        rm1NameL = [rm1.menu_name  for rm1 in dr_m1]
        rm2NameL = [rm2.menu_name  for rm2 in dr_m2]
        rm3NameL = [rm3.menu_name  for rm3 in dr_m3]
        rm4NameL = [rm4.menu_name  for rm4 in dr_m4]
        rm5NameL = [rm5.menu_name  for rm5 in dr_m5]
        rm6NameL = [rm6.menu_name  for rm6 in dr_m6]
        rm7NameL = [rm7.menu_name  for rm7 in dr_m7]
        rm8NameL = [rm8.menu_name  for rm8 in dr_m8]
        
        # dessert name
        sm0NameL = [sm0.menu_name  for sm0 in ds_m0]
        sm1NameL = [sm1.menu_name  for sm1 in ds_m1]
        sm2NameL = [sm2.menu_name  for sm2 in ds_m2]
        sm3NameL = [sm3.menu_name  for sm3 in ds_m3]
        sm4NameL = [sm4.menu_name  for sm4 in ds_m4]
        sm5NameL = [sm5.menu_name  for sm5 in ds_m5]
        sm6NameL = [sm6.menu_name  for sm6 in ds_m6]
        
        context = {
            "dsrtIdList"   : list(dsrtIdList),
            "dsrtNameList" : list(dsrtNameList),
            "drnkIdList"   : list(drnkIdList),
            "drnkNameList" : list(drnkNameList),
            
            "rm0IdL"  : rm0IdL,
            "rm1IdL"  : rm1IdL,
            "rm2IdL"  : rm2IdL,
            "rm3IdL"  : rm3IdL,
            "rm4IdL"  : rm4IdL,
            "rm5IdL"  : rm5IdL,
            "rm6IdL"  : rm6IdL,
            "rm7IdL"  : rm7IdL,
            "rm8IdL"  : rm8IdL,
            
            "sm0IdL"  : sm0IdL,
            "sm1IdL"  : sm1IdL,
            "sm2IdL"  : sm2IdL,
            "sm3IdL"  : sm3IdL,
            "sm4IdL"  : sm4IdL,
            "sm5IdL"  : sm5IdL,
            "sm6IdL"  : sm6IdL,
            
            "rm0NameL"  : rm0NameL,
            "rm1NameL"  : rm1NameL,
            "rm2NameL"  : rm2NameL,
            "rm3NameL"  : rm3NameL,
            "rm4NameL"  : rm4NameL,
            "rm5NameL"  : rm5NameL,
            "rm6NameL"  : rm6NameL,
            "rm7NameL"  : rm7NameL,
            "rm8NameL"  : rm8NameL,

            "sm0NameL"  : sm0NameL,
            "sm1NameL"  : sm1NameL,
            "sm2NameL"  : sm2NameL,
            "sm3NameL"  : sm3NameL,
            "sm4NameL"  : sm4NameL,
            "sm5NameL"  : sm5NameL,
            "sm6NameL"  : sm6NameL,
            
            "nick"         : nick,
            "memid"        : memid,
            "gid"          : gid,
            }
        return HttpResponse(template.render( context, request ) )

    def post(self, request):
        user_id = request.session.get("memid")
        
        comb_reg_ts = datetime.now()
        
        dto = MdComb(
            user_id = user_id,
            comb_tit = request.POST["comb_tit"],
            comb_nop = request.POST["comb_nop"],
            comb_cont = request.POST["comb_cont"],
            comb_img = request.FILES.get("comb_img", ""), 
            comb_reg_ts = comb_reg_ts,
            )
        dto.save()
        
        menu_tag1 = request.POST["select_id_grandchild"]  # 태그 1값
        logger.debug(f'menu_tag1 : {menu_tag1}')
        
        menu_tag2 = request.POST["select_id_grandchild2"]
        logger.debug(f'menu_tag2 : {menu_tag2}')
        
        comb_id = MdComb.objects.filter(user_id = user_id).order_by("-comb_reg_ts").first()
        logger.debug(f'comb_id : {comb_id}')
        
        
        tag1 = MdCombM(
            comb_id = comb_id.comb_id,
            menu_id = menu_tag1,
            )
        tag1.save()
        
        tag2 = MdCombM(
            comb_id = comb_id.comb_id,
            menu_id = menu_tag2,
            )
        tag2.save()
        
        
        return redirect("/md_combi/comblist")      ###### 태그 완료후 이동 주소 수정해야 함

    
    
# 추천글 내용 보기
class CombDView( View ):
    @method_decorator( csrf_exempt )
    def dispatch(self, request, *args, **kwargs):
        return View.dispatch(self, request, *args, **kwargs)

    def get(self, request ):
        template = loader.get_template( "md_combi/combd.html" )
        
        memid   = request.session.get("memid")
        gid     = request.session.get("gid") 
        
        comb_id = request.GET["comb_id"]
        # comb_id = int(comb_id)
        logger.debug(f'comb_id : {comb_id}')
        
        pagenum = request.GET["pagenum"]
        number  = request.GET["number"]
        
        if memid :
            # 로그인한 회원 정보
            user    = MdUser.objects.get( user_id = memid )
            logger.debug(f'user.user_img : {user.user_img}')
            # 선택한 추천조합 정보
            comb    = MdComb.objects.get( comb_id = comb_id )
    
            # 추천글을 작성한 유저의 닉네임
            nick    = MdComb.objects.select_related('user').filter(comb_id = comb_id )
            
            # 선택한 메뉴(태그 값)
            menu    = MdCombM.objects.select_related('comb', 'menu').filter(comb_id = comb_id)
    
            # 추천수
            likeC   = MdCLike.objects.filter(comb = comb_id).count()
            
            # 댓글 갖고있는거 빼옴
            reply   = MdCombR.objects.select_related('user').filter(comb = comb_id).order_by("-c_reply_ts")
            
            # 로그인한 회원이 추천을 했나 안했나 확인용
            comb_like = MdCLike.objects.filter( comb_id = comb_id)
            result = 0
            for like in comb_like :
                if like.user_id == memid :
                    result = 1
                    break
            # logger.debug(f'result : {result}')
                
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
        else:
            comb    = MdComb.objects.get( comb_id = comb_id )
    
            # 추천글을 작성한 유저의 닉네임
            nick    = MdComb.objects.select_related('user').filter(comb_id = comb_id )
            
            # 선택한 메뉴(태그 값)
            menu    = MdCombM.objects.select_related('comb', 'menu').filter(comb_id = comb_id)
    
            # 추천수
            likeC   = MdCLike.objects.filter(comb = comb_id).count()
            
            # 댓글 갖고있는거 빼옴
            reply   = MdCombR.objects.select_related('user').filter(comb = comb_id).order_by("-c_reply_ts")
            
            # 로그인한 회원이 추천을 했나 안했나 확인용
            comb_like = MdCLike.objects.filter( comb_id = comb_id)
            result = 0
            for like in comb_like :
                if like.user_id == memid :
                    result = 1
                    break
            # logger.debug(f'result : {result}')
                
            context = {
                "memid"     : memid,
                "gid"       : gid,
                "pagenum"   :pagenum,
                "number"    : number,
                "comb_id"   : comb_id,
                "comb"      : comb,
                "nick"      : nick,
                "menu"      : menu,
                "likeC"     : likeC,
                "reply"     : reply,
                "comb_like" : comb_like,
                "result"    : result,
                }
            return HttpResponse(template.render( context, request ) )
            
            
            
    def post(self, request ): # 댓글용 ajax....?
        
        memid = request.session.get("memid")
        gid = request.session.get("gid")
        
        comb_id         = request.POST.get("comb_id","")
        pagenum         = request.POST.get("pagenum","")
        number          = request.POST.get("number","")
        c_reply_cont    = request.POST.get("c_reply_cont","")
        
        result = 1                        
        dto = MdCombR(
            comb_id         = comb_id,
            user_id         = memid,
            c_reply_cont    = c_reply_cont,
            c_reply_ts      = datetime.now(),
            )
        dto.save()
            
        return HttpResponse()

# 좋아요 설정 취소
class CLikeView( View ):
    @method_decorator( csrf_exempt )
    def dispatch(self, request, *args, **kwargs):
        return View.dispatch(self, request, *args, **kwargs)
    def post(self, request ):
        
        memid = request.session.get("memid")
        gid = request.session.get("gid")
        
        comb_id = request.POST.get("comb_id","")
        pagenum = request.POST.get("pagenum","")
        number = request.POST.get("number","")
        
        like = MdCLike.objects.filter( user = memid, comb = comb_id ).count()
        
        result = 0
        if like == 0 :
            like = MdCLike(
                comb_id = comb_id,
                user_id = memid,
                like_reg_ts = datetime.now()
                )
            like.save()
            result = 1
        else :
            like = MdCLike.objects.filter( user = memid, comb = comb_id )
            like.delete()
            result = 0
            
        return HttpResponse(result) 
            
    

















    
    