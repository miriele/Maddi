from django.shortcuts import render
from django.views.generic.base import View
from django.http.response import HttpResponse
from django.template import loader
from md_member.models import MdUser
from md_review.models import MdReview

# Create your views here.

class UserlistView(View):
    def get(self,request):
        template = loader.get_template("md_admin/userlist.html")
        count = MdUser.objects.count() #회원수  
        users = MdUser.objects.select_related("user_g").only("user_id","user_name","user_g__user_g_name","user_reg_ts")#회원리스트   
        context ={
            "count":count,
            "users":users,
            }
        return HttpResponse(template.render(context,request))

class UserinfoView(View):
    def get(self,request):
        template = loader.get_template("md_admin/userinfo.html")
        id = request.GET["id"]
        users = MdUser.objects.select_related("user_g").select_related("user_g").get(user_id=id)
        context ={
            "id":id,
            "users":users,
             }
        return HttpResponse(template.render(context,request))
    
class ReviewlistView(View):
    def get(self,request):
        template = loader.get_template("md_admin/reviewlist.html")
        count = MdReview.objects.count()    #리뷰갯수
        #리뷰리스트
        rdtos = MdReview.objects.select_related("ordr")
        #리뷰리스트에서 아이디,주문번호,매장명까지 출력성공 매장명 출력은 orm 수정이 필요함
        context ={
            "count":count,
            "rdtos":rdtos,
            }
        return HttpResponse(template.render(context,request))
    
class ReviewinfoView(View):
    def get(self,request):
        template = loader.get_template("md_admin/reviewinfo.html")
        context ={
            }
        return HttpResponse(template.render(context,request))
    
class SregistlistView(View):
    def get(self,request):
        template = loader.get_template("md_admin/sregistlist.html")
        context ={
            }
        return HttpResponse(template.render(context,request))
    
class SregistinfoView(View):
    def get(self,request):
        template = loader.get_template("md_admin/sregistinfo.html")
        context ={
            }
        return HttpResponse(template.render(context,request))   