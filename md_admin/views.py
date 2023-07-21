from django.shortcuts import render
from django.views.generic.base import View
from django.http.response import HttpResponse
from django.template import loader
from md_member.models import MdUser

# Create your views here.

class UserlistView(View):
    def get(self,request):
        template = loader.get_template("md_admin/userlist.html")
        count = MdUser.objects.count()   
        users = MdUser.objects.select_related("user_g").only("user_id","user_name","user_g__user_g_name","user_reg_ts")    
        context ={
            "count":count,
            "users":users,
            }
        return HttpResponse(template.render(context,request))

class UserinfoView(View):
    def get(self,request):
        template = loader.get_template("md_admin/userinfo.html")
        id = request.GET["id"]
        print(id)
        users = MdUser.objects.select_related("user_g").select_related("user_g").get(user_id=id)
        context ={
            "id":id,
            "users":users,
             }
        return HttpResponse(template.render(context,request))
    
class ReviewlistView(View):
    def get(self,request):
        template = loader.get_template("md_admin/userlist.html")
        context ={
            }
        return HttpResponse(template.render(context,request))
    
class ReviewinfoView(View):
    def get(self,request):
        template = loader.get_template("md_admin/userlist.html")
        context ={
            }
        return HttpResponse(template.render(context,request))
    
class SregistlistView(View):
    def get(self,request):
        template = loader.get_template("md_admin/userlist.html")
        context ={
            }
        return HttpResponse(template.render(context,request))
    
class SregistinfoView(View):
    def get(self,request):
        template = loader.get_template("md_admin/userlist.html")
        context ={
            }
        return HttpResponse(template.render(context,request))   