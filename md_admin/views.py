from django.shortcuts import render, redirect
from django.views.generic.base import View
from django.http.response import HttpResponse
from django.template import loader
from md_member.models import MdUser, MdUserG
from md_review.models import MdReview, MdTag, MdRevT
from md_order.models import MdOrdr, MdOrdrM
from md_store.models import MdStorReg, MdStorM, MdStorT
import logging
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.utils.dateformat import DateFormat
from datetime import datetime
from django.db.models.aggregates import Count


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
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return View.dispatch(self, request, *args, **kwargs)
        
    def get(self,request):
        template = loader.get_template("md_admin/userinfo.html")
        id = request.GET["id"]
        users = MdUser.objects.select_related("user_g").get(user_id=id)
            
        context ={
            "id":id,
            "users":users,  
             }
        return HttpResponse(template.render(context,request))
    #회원등급수정
    def post(self,request):
        id = request.POST["id"]
        usrg = MdUserG.objects.get(user_g_id=request.POST["user_g"])
        users = MdUser.objects.get(user_id=id)
        
        # logger.debug(f'usrg : {usrg}')
        
        newusers=MdUser(
            user_id = id,
            user_name = users.user_name,
            user_pass = users.user_pass,
            user_img = users.user_img,
            gen = users.gen,
            user_nick = users.user_nick,
            user_bir = users.user_bir,
            user_reg_ts = users.user_reg_ts,
            user_g = usrg,                    
        )
        newusers.save()
           
        return redirect("/md_admin/userlist")

class ReviewlistView(View):
    def get(self,request):
        template = loader.get_template("md_admin/reviewlist.html")
        count = MdReview.objects.count()    #리뷰갯수
        
        # 화면에 출력해줄 내용
        # : 사용자명, 주문번호, 매장명, 리뷰등록일
        # : md_ordr.user_id, md_ordr.ordr_id, md_stor.stor_name, md_review.rev_ts
        
        # select * from md_review;(김민우)
        # select * from md_ordr where ordr_id=1;(김민우)
        # select * from md_ordr_m where ordr_id=1;(김민우)
        # select * from md_stor_m where stor_m_id=15;(김민우)
        # select * from md_stor where stor_id=1;(김민우)
            
        rdtos = MdReview.objects.select_related('ordr__mdordrm__stor_m__stor').values('rev_id','ordr__user__user_id', 'ordr_id', 'ordr__mdordrm__stor_m__stor__stor_name', 'rev_ts')

        #logger.debug(f'type(rdtos) : {type(rdtos)}\nrdtos : {rdtos}')
        
        context ={
            "count":count,
            "rdtos":rdtos,
            }
        return HttpResponse(template.render(context,request))
    
class ReviewinfoView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return View.dispatch(self, request, *args, **kwargs)
    
    def get(self,request):
        template = loader.get_template("md_admin/reviewinfo.html")
        rev_id = request.GET["rev_id"]
        
        #화면에 출력해줄 내용
        #태그는 태그분류없이 나열
        #리뷰이미지,    메장메뉴명,    리뷰별점,    태그명,    리뷰내용 
        #md_review.rev_img,   md_stro_m.stor_m_name,    md_review.rev_star    md_tag.tag_name    md_review.rev_cont
        
        # stor_m_id 를 받아오는 곳은 없어서 일단 하드코딩 해둠, 수정필요~!
        #SELECT stor_m_name FROM md_stor_m WHERE stor_m_id = 15;(김민우)
        storm = MdStorM.objects.filter(stor_m_id=15).values('stor_m_name')
        
        if storm.exists() :
            stor_m_name = storm.first()['stor_m_name']
            logger.debug(f'stor_m_name : {stor_m_name}')
        else:
            logger.debug(f'stor_m_name : 해당하는 레코드가 없습니다')
        
        #SELECT rev_img,rev_star,rev_cont FROM md_review WHERE rev_id = 1;(김민우)
        reviewn = MdReview.objects.filter(rev_id=rev_id).values('rev_img', 'rev_star', 'rev_cont')
        
        if reviewn.exists() :
            rev_img  = reviewn.first()['rev_img']
            rev_star = reviewn.first()['rev_star']
            rev_cont = reviewn.first()['rev_cont']
            logger.debug(f'rev_img : {rev_img}\trev_star : {rev_star}\trev_cont : {rev_cont}\n')
        else:
            logger.debug(f'rev_img, rev_star, rev_cont : 해당하는 레코드가 없습니다')
        
        
        #SELECT t.tag_name FROM md_tag t JOIN md_rev_t rt ON t.tag_id = rt.tag_id WHERE rt.rev_id = 1;(김민우)
        tagn = MdTag.objects.filter(mdrevt__rev_id=rev_id).values('tag_name')
        
        if tagn.exists() :
            for item in tagn :
                tag_name = item['tag_name']
                logger.debug(f'tag_name : {tag_name}')
        else:
            logger.debug(f'tag_name : 해당하는 레코드가 없습니다')

        context ={
            "rev_id":rev_id,
            "strom":storm,
            "reviewn":reviewn,
            "tagn":tagn,
            }
        return HttpResponse(template.render(context,request))
   
    #리뷰삭제 
    def post(self,request):
        rev_id = request.POST["rev_id"]
        #리뷰태그 삭제
        tdto = MdRevT.objects.filter(rev=rev_id)
        tdto.delete()
        #리뷰삭제
        rdto = MdReview.objects.get(rev_id=rev_id)
        rdto.delete()
        return redirect("/md_admin/reviewlist")
        
        
class SregistlistView(View):
    def get(self,request):
        template = loader.get_template("md_admin/sregistlist.html")
        reglists = MdStorReg.objects.select_related("stor")
        context ={
            "reglists":reglists,
            }
        return HttpResponse(template.render(context,request))
    
class SregistinfoView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return View.dispatch(self, request, *args, **kwargs)
        
    def get(self,request):
        template = loader.get_template("md_admin/sregistinfo.html")
        reg_id = request.GET["reg_id"]
        reginfo = MdStorReg.objects.get(reg_id=reg_id)
        #화면에 출력해줄내용
        #아이디/매장명/매장유형/사업자등록번호/등록신청일/사업자등록이미지
        
        # 매장유형명만출력하면 가능 (김민우)
        # SELECT stor_id FROM md_stor_reg WHERE reg_id = 5;
        # SELECT stor_t_id FROM md_stor WHERE stor_id = 100;
        # SELECT stor_t_name FROM md_stor_t WHERE stor_t_id = 21;

        # select stor_t_name (김민우)
        # from md_stor_reg sr, md_stor s, md_stor_t st
        # where  sr.stor_id = s.stor_id
        #     and s.stor_t_id = st.stor_t_id
        #     and sr.reg_id = 5;
        result = MdStorT.objects.filter(mdstor__mdstorreg__reg_id=reg_id).values('stor_t_name')

        # if result.exists() :
        #     stor_t_name = result.first()['stor_t_name']
        #     logger.debug(f'stor_t_name : {stor_t_name}')
        # else:
        #     logger.debug(f'stor_t_name : 해당하는 레코드가 없습니다')

        context ={
            "reg_id":reg_id,          
            "reginfo":reginfo,
            "result":result,
            }
        return HttpResponse(template.render(context,request))
    
    #점주등록신청 승인
    def post(self,request):
        reg_id = request.POST["reg_id"]
        reginfo = MdStorReg.objects.get(reg_id=reg_id)
        
        regagree = MdStorReg(
            reg_id = reg_id,
            user = reginfo.user,
            stor = reginfo.stor,
            reg_num = reginfo.reg_num,
            reg_img = reginfo.reg_img,
            reg_sub_ts = reginfo.reg_sub_ts,
            reg_con_ts = datetime.now(),
            )
        regagree.save()
        #등록신청한 회원의 등급 -> 6(점주)로 수정     
        id = request.POST["id"]
        users = MdUser.objects.filter(user_id=id).update(user_g=6)
        
         
        return redirect("/md_admin/sregistlist")
        
class GenstatisView(View):
    def get(self,request):
        template = loader.get_template("md_admin/genstatis.html")
        count = MdUser.objects.count()
        labels = []
        data = []
        #남/여 count
        gen = MdUser.objects.select_related('gen').values('gen__gen_name').annotate(Count('gen'))
        print(gen.values())

        context = {
            "gen":gen,
            "count":count,
            }
        return HttpResponse(template.render(context,request))