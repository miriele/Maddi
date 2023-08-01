from django.shortcuts import render, redirect
import logging
from django.views.generic.base import View
from django.template import loader
from django.http.response import HttpResponse
from django.utils.decorators import method_decorator
from datetime import datetime
from md_member.models import MdUser, MdUDsrt, MdIntrT, MdTastT, MdUDrnk, MdUAlgy,\
    MdUIntr, MdUTast, MdUserG
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist
from md_store.models import MdAlgyT, MdDrnkT, MdDsrtT, MdStorM, MdStor
from md_order.models import MdOrdr, MdOrdrM
from md_review.models import MdReview

# 로그
logger = logging.getLogger( __name__ )

# 로그인
class LoginView( View ):
    @method_decorator( csrf_exempt )
    def dispatch(self, request, *args, **kwargs):
        return View.dispatch(self, request, *args, **kwargs)
    def get(self, request ):
        template = loader.get_template( "md_member/login.html" )
        context = {}
        return HttpResponse(template.render( context, request ) )
    def post(self, request ):
        user_id = request.POST["user_id"]
        user_pass = request.POST["user_pass"]
        try :
            dto = MdUser.objects.get( user_id = user_id )
            if user_pass == dto.user_pass :
                request.session["memid"] = user_id;
                request.session["gid"] = dto.user_g_id;
                return redirect("/md_main/main") 
            else :
                message = "입력하신 비밀번호가 다릅니다"
        except ObjectDoesNotExist :
            message = "입력하신 아이디가 없습니다"
        template = loader.get_template( "md_member/login.html" )
        context = {
                "message" : message
            }
        return HttpResponse(template.render( context, request ) )

# 로그아웃
class LogoutView( View ):
    def get(self, request ):
        del request.session["memid"]
        del request.session["gid"]
        return redirect( "/md_main/main" )

# 회원가입    
class InputView ( View ):
    @method_decorator( csrf_exempt )
    def dispatch(self, request, *args, **kwargs):
        return View.dispatch(self, request, *args, **kwargs)
    def get(self, request ):
        md_dsrt_t = MdDsrtT.objects.filter(dsrt_t_id__gt=-1 ).order_by("dsrt_t_id")
        md_drnk_t = MdDrnkT.objects.filter(drnk_t_id__gt=-1).order_by("drnk_t_id")
        md_algy_t = MdAlgyT.objects.order_by("algy_t_id")
        md_intr_t = MdIntrT.objects.order_by("intr_t_id" )
        md_tast_t = MdTastT.objects.order_by("tast_t_id")
       
        template = loader.get_template( "md_member/input.html" )
        context = {
            "md_dsrt_t" : md_dsrt_t,
            "md_drnk_t" : md_drnk_t,
            "md_algy_t" : md_algy_t,
            "md_intr_t" : md_intr_t,
            "md_tast_t" : md_tast_t,
            }
        return HttpResponse( template.render( context, request ) )

    def post(self, request):
        user_id  = request.POST["user_id"]
        user_img = request.FILES.get("user_img")    

        # 이미지 업로드 안 했을 시 기본으로 저장
        if user_img  == None :
            user_img = "default_user.jpg"
        else :
            user_img 
        
        dtos = MdUser(
            user_id     = user_id,
            user_pass   = request.POST["user_pass"],
            user_name   = request.POST["user_name"],
            user_nick   = request.POST["user_nick"],
            user_bir    = request.POST["user_bir"],
            gen_id      = request.POST["gen_id"],
            user_img    = user_img,
            user_g_id   = 1,
            user_reg_ts = datetime.now(),
            )
        dtos.save()
        
        # 태그 
        list_dsrt = request.POST.getlist("md_dsrt_t")
        list_drnk = request.POST.getlist("md_drnk_t")
        list_algy = request.POST.getlist("md_algy_t")
        list_intr = request.POST.getlist("md_intr_t")
        list_tast = request.POST.getlist("md_tast_t") 
        
        if list_dsrt :
            for a in list_dsrt :
                dto = MdUDsrt(
                    user_id   = user_id,
                    dsrt_t_id = a
                    )
                dto.save()
        
        if list_drnk :
            for b in list_drnk :
                dto = MdUDrnk(
                    user_id   = user_id,
                    drnk_t_id = b
                    )
                dto.save()
        
        if list_algy :
            for c in list_algy :
                dto = MdUAlgy(
                    user_id   = user_id,
                    algy_t_id = c
                    )
                dto.save()
        
        if list_intr :
            for d in list_intr :
                dto = MdUIntr(
                    user_id   = user_id,
                    intr_t_id = d
                    )
                dto.save()
        
        if list_tast :
            for e in list_tast :
                dto = MdUTast(
                    user_id   = user_id,
                    tast_t_id = e
                    )
                dto.save()
        
        return redirect( "/md_member/login" )

# 아이디 중복체크
class IdCheckView( View ):
    def get(self, request ):
        user_id = request.GET.get("user_id", "")
        idcount = MdUser.objects.filter(user_id=user_id ).count()
        # idcount = MdUser.objects.filter(user_id=user_id ).annotate( Count("user_id"))
        # if idcount.count() > 0 :    >이거는 queryset방식  위에꺼 처럼 쓰면 쿼리셋 방식이 되서 서로 타입이 안 맞아 비교할수 없다 나옴
        result = 0
        if idcount > 0 :
            result = 1 
        else :
            result = 0

        return HttpResponse(result)

# 닉네임 중복체크
class NickCheckView( View ):
    def get(self, request ):
        user_nick = request.GET.get("iuser_nick")
        nickcount = MdUser.objects.filter(user_nick=user_nick ).count()
        result = 0
        if nickcount > 0 :
            result = 1 
        else :
            result = 0

        return HttpResponse(result)
         
# 회원정보 보기& 수정
class UserInfoView( View ):
    @method_decorator( csrf_exempt )
    def dispatch(self, request, *args, **kwargs):
        return View.dispatch(self, request, *args, **kwargs)
    def get(self, request ):
        memid = request.session.get("memid")
        gid = request.session.get("gid")

        dtos = MdUser.objects.get(user_id = memid)
        g_name = MdUserG.objects.get(user_g_id = gid )
        
        md_dsrt_t = MdDsrtT.objects.filter(dsrt_t_id__gt=-1 ).order_by("dsrt_t_id")
        md_drnk_t = MdDrnkT.objects.filter(drnk_t_id__gt=-1).order_by("drnk_t_id")
        md_algy_t = MdAlgyT.objects.order_by("algy_t_id")
        md_intr_t = MdIntrT.objects.order_by("intr_t_id")
        md_tast_t = MdTastT.objects.order_by("tast_t_id")
        
        udsrt = MdUDsrt.objects.filter(user_id = memid )
        udrnk = MdUDrnk.objects.filter(user_id = memid )
        ualgy = MdUAlgy.objects.filter(user_id = memid )
        uintr = MdUIntr.objects.filter(user_id = memid )
        utast = MdUTast.objects.filter(user_id = memid )
       
        template = loader.get_template( "md_member/userinfo.html")
        context = {
            "memid"     : memid,
            "gid"       :gid,
            
            "dtos"      :dtos,
            "g_name"    :g_name,
            "md_intr_t" : md_intr_t,
            "md_tast_t" : md_tast_t,
            "md_algy_t" : md_algy_t,
            "md_drnk_t" : md_drnk_t,
            "md_dsrt_t" : md_dsrt_t,
            "udsrt"     : udsrt,
            "udrnk"     : udrnk,
            "ualgy"     : ualgy,
            "uintr"     : uintr,
            "utast"     : utast,
            }       
        
        return HttpResponse( template.render( context, request ) )
    def post(self, request ):
        user_id = request.POST["user_id"]
        dto = MdUser.objects.get(user_id = user_id)
        user_img = request.FILES.get("user_img")  
        
        logger.debug(user_img)  
        # 이미지 업로드 안 했을 시 기본으로 저장
        if user_img  == None :
            user_img = "default_user.jpg"
        else :
            user_img 
            
        logger.debug(user_img)
        ndtos = MdUser(
            user_id = user_id,
            user_pass = request.POST["user_pass"],
            user_name = request.POST["user_name"],
            user_nick = request.POST["user_nick"],
            user_bir = request.POST["user_bir"],
            gen_id = request.POST["gen_id"],
            user_img = user_img,
            user_g_id = dto.user_g_id,
            user_reg_ts = dto.user_reg_ts
            )      
        ndtos.save()
        
        # 태그 받아온거
        list_dsrt = request.POST.getlist("md_dsrt_t")
        logger.debug(list_dsrt)
        list_drnk = request.POST.getlist("md_drnk_t")
        list_algy = request.POST.getlist("md_algy_t")
        list_intr = request.POST.getlist("md_intr_t")
        list_tast = request.POST.getlist("md_tast_t") 
        # 태그 디비서 가져온거 
        udsrt = MdUDsrt.objects.filter(user_id = user_id )
        udrnk = MdUDrnk.objects.filter(user_id = user_id )
        ualgy = MdUAlgy.objects.filter(user_id = user_id )
        uintr = MdUIntr.objects.filter(user_id = user_id )
        utast = MdUTast.objects.filter(user_id = user_id )

        for ds in udsrt :
            ds.delete()
           
        for a in list_dsrt :
            if a :
                dtoa = MdUDsrt(
                    user_id = user_id,
                    dsrt_t_id = a
                    )
                dtoa.save()

        for dr in udrnk :
            dr.delete()
        for b in list_drnk :
            if b:
                dtob = MdUDrnk(
                    user_id = user_id,
                    drnk_t_id = b
                    )
                dtob.save()
        
        for al in ualgy :
            al.delete()
        for c in list_algy :
            if c:
                dtoc = MdUAlgy(
                    user_id = user_id,
                    algy_t_id = c
                    )
                dtoc.save()

        for int in uintr :
            int.delete()
        for d in list_intr :
            if d:
                dtod = MdUIntr(
                    user_id = user_id,
                    intr_t_id = d
                    )
                dtod.save()
        
        for ta in utast :
            ta.delete()
        for e in list_tast :
            if e:
                dtoe = MdUTast(
                    user_id = user_id,
                    tast_t_id = e
                    )
                dtoe.save()
        return redirect("/md_member/userinfo")
    
    
    
page_size = 20
page_block = 3    
class MyOrderListView( View ):
    def get(self, request ):
        
        template = loader.get_template( "md_member/myorderlist.html")
        
        memid   = request.session.get("memid")
        gid     = request.session.get("gid")
        
        # 갯수 있나 없나
        count = MdOrdr.objects.filter( user_id= memid ).count()
        
        if count == 0 :
            context = {
                "count" :count,
                "memid" :memid,
                "gid" :gid,
                }
        else :   
            pagenum = request.GET.get( "pagenum" )
            
            if not pagenum :
                pagenum = "1"
            
            pagenum = int( pagenum )                            #5
            start   = (pagenum -1 ) * int( page_size )            #4*5=    20
            end     = start + int( page_size )                      #20+5=    25
            
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
            
            pages = range(startpage, endpage + 1)
            
            # 주문 번호 / 매장명 / 주문메뉴 / 총 금액 >ordr_num|mul:stor_m_pric /주문일시 /주문 완료일/+리뷰 작성일?리뷰의 주문 아이디?
            odtos = MdOrdr.objects.select_related('mdordrm__stor_m__stor').filter(user_id = memid).order_by("-ordr_id").values('ordr_id', 'mdordrm__stor_m__stor__stor_name', 'mdordrm__stor_m__stor_m_name', 'mdordrm__ordr_num', 'mdordrm__stor_m__stor_m_pric', 'ordr_ord_ts', 'ordr_com_ts')[start:end]
            
            # 리뷰 버튼
            rev = MdReview.objects.select_related('ordr').filter(ordr__user_id = memid ).values('ordr_id')
            logger.debug(f' rev : { rev  }')
            #  logger.debug(f' review : { "리뷰 없음"  }')
                        
            
            
            
            # rev_list = list(rev)
            # rev_id_ele = list([m['ordr_id'] for m in rev_list])
            # print(rev_id_ele)
                
            # for o in odtos:
            #     for r in rev:
            #         logger.debug(f' r  : { r.ordr_id }')
            # ordr_id.append(r)
            # logger.debug(f' r  : {ordr_id}')
        

            context = {
                "odtos"     : odtos,
                "rev"       : rev,
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
        
        
        
        
        
