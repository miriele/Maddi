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


# 로그
logger = logging.getLogger( __name__ )

class UserlistView(View):
    def get(self,request):
        template = loader.get_template("md_admin/userlist.html")
        count = MdUser.objects.count() #회원수  
        users = MdUser.objects.select_related("user_g").only("user_id","user_name","user_g__user_g_name","user_reg_ts") #회원리스트
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
        if newusers.user_g ==2:
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
            user_ext_ts = DateFormat(datetime.now()),      
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
        
        # select o.user_id, o.ordr_id, s.stor_name, r.rev_ts
        # from md_review r, md_ordr o,
        #      md_ordr_m om, md_stor_m sm, md_stor s
        # where  r.ordr_id    = o.ordr_id
        #     and o.ordr_id    = om.ordr_id
        #     and om.stor_m_id = sm.stor_m_id
        #     and sm.stor_id   = s.stor_id
        #     and r.rev_id     = 1;            

        # rev_id를 얻어오는 부분이 없어서 하드코딩 해놓음. 수정해야 함~!
        # rdtos = MdReview.objects.select_related('ordr__mdordrm__stor_m__stor').values('ordr__user__user_id', 'ordr_id', 'ordr__mdordrm__stor_m__stor__stor_name', 'rev_ts')
        rdtos = MdReview.objects.filter(rev_id=1).select_related('ordr__mdordrm__stor_m__stor').values('ordr__user__user_id', 'ordr_id', 'ordr__mdordrm__stor_m__stor__stor_name', 'rev_ts')

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
        
        # stor_m_id 를 받아오는 곳은 없어서 일단 하드코딩 해둠, 수정필요~!
        #SELECT stor_m_name FROM md_stor_m WHERE stor_m_id = 15;
        result = MdStorM.objects.filter(stor_m_id=15).values('stor_m_name')
        
        if result.exists() :
            stor_m_name = result.first()['stor_m_name']
            logger.debug(f'stor_m_name : {stor_m_name}')
        else:
            logger.debug(f'stor_m_name : 해당하는 레코드가 없습니다')
        
        #SELECT rev_img,rev_star,rev_cont FROM md_review WHERE rev_id = 1;
        result = MdReview.objects.filter(rev_id=revid).values('rev_img', 'rev_star', 'rev_cont')
        
        if result.exists() :
            rev_img  = result.first()['rev_img']
            rev_star = result.first()['rev_star']
            rev_cont = result.first()['rev_cont']
            logger.debug(f'rev_img : {rev_img}\trev_star : {rev_star}\trev_cont : {rev_cont}\n')
        else:
            logger.debug(f'rev_img, rev_star, rev_cont : 해당하는 레코드가 없습니다')
        
        
        #SELECT t.tag_name FROM md_tag t JOIN md_rev_t rt ON t.tag_id = rt.tag_id WHERE rt.rev_id = 1;
        result = MdTag.objects.filter(mdrevt__rev_id=revid).values('tag_name')
        
        if result.exists() :
            for item in result :
                tag_name = item['tag_name']
                logger.debug(f'tag_name : {tag_name}')
        else:
            logger.debug(f'tag_name : 해당하는 레코드가 없습니다')

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
        
        # 매장유형명만출력하면 가능
        # SELECT stor_id FROM md_stor_reg WHERE reg_id = 5;
        # SELECT stor_t_id FROM md_stor WHERE stor_id = 100;
        # SELECT stor_t_name FROM md_stor_t WHERE stor_t_id = 21;

        # select stor_t_name
        # from md_stor_reg sr, md_stor s, md_stor_t st
        # where  sr.stor_id = s.stor_id
        #     and s.stor_t_id = st.stor_t_id
        #     and sr.reg_id = 5;
        result = MdStorT.objects.filter(mdstor__mdstorreg__reg_id=regid).values('stor_t_name')

        if result.exists() :
            stor_t_name = result.first()['stor_t_name']
            logger.debug(f'stor_t_name : {stor_t_name}')
        else:
            logger.debug(f'stor_t_name : 해당하는 레코드가 없습니다')

        context ={
            "regid":regid,
            "reginfo":reginfo,
            }
        return HttpResponse(template.render(context,request))   