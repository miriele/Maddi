from django.shortcuts import render, redirect
import logging
from django.views.generic.base import View
from django.template import loader
from django.http.response import HttpResponse
from django.utils.decorators import method_decorator
from django.utils.dateformat import DateFormat
from datetime import datetime
from md_member.models import MdUser, MdUDsrt, MdIntrT, MdTastT
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist
from md_store.models import MdAlgyT, MdDrnkT, MdDsrtT

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
        user_g_id = request.POST["user_g_id"]
        try :
            dto = MdUser.objects.get( user_id = user_id )
            if user_pass == dto.user_pass :
                request.session["memid"] = user_id;
                request.session["gid"] = user_g_id;
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
        md_intr_t = MdIntrT.objects.order_by("intr_t_id")
        md_tast_t = MdTastT.objects.order_by("tast_t_id")
        md_algy_t = MdAlgyT.objects.order_by("algy_t_id")
        md_drnk_t = MdDrnkT.objects.order_by("drnk_t_id")
        md_dsrt_t = MdDsrtT.objects.order_by("dsrt_t_id")
       
        template = loader.get_template( "md_member/input.html" )
        context = {
            "md_intr_t" : md_intr_t,
            "md_tast_t" : md_tast_t,
            "md_algy_t" : md_algy_t,
            "md_drnk_t" : md_drnk_t,
            "md_dsrt_t" : md_dsrt_t,
            }
        return HttpResponse( template.render( context, request ) )


# 회원정보 보기& 수정
class UserInfoView( View ):
    @method_decorator( csrf_exempt )
    def dispatch(self, request, *args, **kwargs):
        return View.dispatch(self, request, *args, **kwargs)
    def get(self, request ):
        memid = request.session.get("memid")
        dtos = MdUser.objects.get(user_id = memid)
        
        md_intr_t = MdIntrT.objects.order_by("intr_t_id")
        md_tast_t = MdTastT.objects.order_by("tast_t_id")
        md_algy_t = MdAlgyT.objects.order_by("algy_t_id")
        md_drnk_t = MdDrnkT.objects.order_by("drnk_t_id")
        md_dsrt_t = MdDsrtT.objects.order_by("dsrt_t_id")
        
        template = loader.get_template( "md_member/userinfo.html")
        context = {
            "memid" : memid,
            "dtos" :dtos, 
            "md_intr_t" : md_intr_t,
            "md_tast_t" : md_tast_t,
            "md_algy_t" : md_algy_t,
            "md_drnk_t" : md_drnk_t,
            "md_dsrt_t" : md_dsrt_t,
            }       
        return HttpResponse( template.render( context, request ) )
