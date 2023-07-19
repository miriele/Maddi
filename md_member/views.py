from django.shortcuts import render, redirect
import logging
from django.views.generic.base import View
from django.template import loader
from django.http.response import HttpResponse
from django.utils.decorators import method_decorator
from django.utils.dateformat import DateFormat
from datetime import datetime
from md_member.models import MdUser, MdUDsrt, MdIntrT, MdTastT, MdUDrnk, MdUAlgy,\
    MdUIntr, MdUTast, MdUserG
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist
from md_store.models import MdAlgyT, MdDrnkT, MdDsrtT
from django.db.models.aggregates import Count

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
        
        user_id = request.POST["user_id"]
        user_img = request.FILES.get("user_img")    
        # 이미지 업로드 안 했을 시 기본으로 저장
        if user_img  == None :
            user_img = "default_user.jpg"
        else :
            user_img 
        
        dtos = MdUser(
            user_id = user_id,
            user_pass = request.POST["user_pass"],
            user_name = request.POST["user_name"],
            user_nick = request.POST["user_nick"],
            user_bir = request.POST["user_bir"],
            gen_id = request.POST["gen_id"],
            user_img = user_img,
            user_g_id = 1,
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
                    user_id = user_id,
                    dsrt_t_id = a
                    )
                dto.save()
        if list_drnk :
            for b in list_drnk :
                dto = MdUDrnk(
                    user_id = user_id,
                    drnk_t_id = b
                    )
                dto.save()
        if list_algy :
            for c in list_algy :
                dto = MdUAlgy(
                    user_id = user_id,
                    algy_t_id = c
                    )
                dto.save()
        if list_intr :
            for d in list_intr :
                dto = MdUIntr(
                    user_id = user_id,
                    intr_t_id = d
                    )
                dto.save()
        if list_tast :
            for e in list_tast :
                dto = MdUTast(
                    user_id = user_id,
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
            "memid" : memid,
            "dtos" :dtos,
            "g_name" :g_name,
            "md_intr_t" : md_intr_t,
            "md_tast_t" : md_tast_t,
            "md_algy_t" : md_algy_t,
            "md_drnk_t" : md_drnk_t,
            "md_dsrt_t" : md_dsrt_t,
            "udsrt" : udsrt,
            "udrnk" : udrnk,
            "ualgy" : ualgy,
            "uintr" : uintr,
            "utast" : utast,
            }       
        return HttpResponse( template.render( context, request ) )
