from django.shortcuts import render
from django.views.generic.base import View
from django.http.response import HttpResponse
from django.template import loader
from md_member.models import MdUser
from md_review.models import MdReview, MdTag, MdRevT
from md_order.models import MdOrdr, MdOrdrM
from md_store.models import MdStorReg
import logging


# 로그
logger = logging.getLogger( __name__ )

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
            
        rdtos = MdReview.objects.select_related('ordr__mdordrm__stor_m__stor').values('ordr__user__user_id', 'ordr_id', 'ordr__mdordrm__stor_m__stor__stor_name', 'rev_ts')

        logger.debug(f'type(rdtos) : {type(rdtos)}\nrdtos : {rdtos}')
        
        context ={
            "count":count,
            "rdtos":rdtos,
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
        reglists = MdStorReg.objects.select_related("stor")
        context ={
            "reglists":reglists,
            }
        return HttpResponse(template.render(context,request))
    
class SregistinfoView(View):
    def get(self,request):
        template = loader.get_template("md_admin/sregistinfo.html")
        regid = request.GET["regid"]
        reginfo = MdStorReg.objects.get(reg_id=regid)
        #화면에 출력해줄내용
        #아이디/매장명/매장유형/사업자등록번호/등록신청일/사업자등록이미지
        
        #매장유형명만출력하면 가능
        #SELECT stor_id FROM md_stor_reg WHERE reg_id = 5;
        #SELECT stor_t_id FROM md_stor WHERE stor_id = 100;
        #SELECT stor_t_name FROM md_stor_t WHERE stor_t_id = 21;

        context ={
            "regid":regid,
            "reginfo":reginfo,
            }
        return HttpResponse(template.render(context,request))   