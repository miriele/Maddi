from django.shortcuts import render
from django.views.generic.base import View
from django.http.response import HttpResponse
from django.template import loader
from md_member.models import MdUser
from md_review.models import MdReview, MdTag, MdRevT
from md_order.models import MdOrdr, MdOrdrM

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
        
        # 화면에 출력해줄 내용
        # : 사용자명, 주문번호, 매장명, 리뷰등록일
        # : md_ordr.user_id, md_ordr.ordr_id, md_stor.stor_name, md_review.rev_ts
        
        # select * from md_review;
        # select * from md_ordr where ordr_id=1;
        # select * from md_ordr_m where ordr_id=1;
        # select * from md_stor_m where stor_m_id=15;
        # select * from md_stor where stor_id=1;
            
        context ={
            "count":count,
            }
        return HttpResponse(template.render(context,request))
    
class ReviewinfoView(View):
    def get(self,request):
        template = loader.get_template("md_admin/reviewinfo.html")
        revid = request.GET["revid"]
        
        #화면에 출력해줄 내용
        #태그는 태그분류없이 나열
        #리뷰이미지,    메장메뉴명,    리뷰별점,    태그명,    리뷰내용 
        #md_review.rev_img,   md_stro_m.stor_m_name,    md_review.rev_star    md_tag.tag_name    md_review.rev_cont
        
        #SELECT * FROM md_stor_m WHERE stor_m_id = 15;
        #SELECT rev_img,rev_star,rev_cont FROM md_review WHERE rev_id = 1;
        #SELECT t.tag_name FROM md_tag t JOIN md_rev_t rt ON t.tag_id = rt.tag_id WHERE rt.rev_id = 1;
        
        context ={
            "revid":revid,
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