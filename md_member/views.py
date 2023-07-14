from django.shortcuts import render, redirect
import logging
from django.views.generic.base import View
from django.template import loader
from django.http.response import HttpResponse
from django.utils.decorators import method_decorator
from django.utils.dateformat import DateFormat
from datetime import datetime
from md_member.models import MdUser
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist

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
    
class LogoutView( View ):
    def get(self, request ):
        del request.session["memid"]
        del request.session["gid"]
        return redirect( "/md_main/main" )
    
class InputView ( View ):
    def get(self, request ):
        template = loader.get_template( "md_member/input.html" )
        context = {}
        return HttpResponse( template.render( context, request ) )


