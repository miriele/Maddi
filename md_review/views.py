from django.shortcuts import render, redirect
from django.template import loader
from django.views.generic.base import View
from django.http.response import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from datetime import datetime
import logging
from md_review.models import MdReview, MdTag, MdRevT
from md_member.models import MdUser
from md_order.models import MdOrdrM, MdOrdr
from md_store.models import MdStorM

# 로그
logger = logging.getLogger( __name__ )


# 리뷰 보기 폼>매뉴 정보페이지에 합체
class ReviewView( View ):
    def get(self, request ):
        template = loader.get_template( "md_review/review.html" )   ########
        
        memid = request.session.get("memid")
        gid = request.session.get("gid")
        
        stor_id = request.GET["stor_id"]
        
        stor_id = int(stor_id)
        logger.debug(f' stor_id  : { stor_id }')
        
        count   = MdReview.objects.count()      #나옴
        
        rdtos   = MdReview.objects.select_related('ordr__mdordrm__stor_m__stor__user').values('rev_id','ordr__user__user_id', 'ordr_id', 'ordr__mdordrm__stor_m__stor__stor_name','ordr__mdordrm__stor_m__stor_id', 'rev_ts', 'ordr__user__user_nick', "ordr__user__user_img", 'rev_cont', 'rev_star', 'rev_img')
        # logger.debug(f' rdtos  : { rdtos }')
        
        tags    = MdRevT.objects.select_related('tag', 'rev').values('tag__tag_name', 'rev__rev_id')
        
        user    = MdOrdr.objects.select_related('user')
        # logger.debug(f' user  : { user }')
        context = {
            "memid"     : memid,
            "gid"       : gid,
            "stor_id"   : stor_id,
            "tags"      : tags,
            "count"     : count,
            "rdtos"     : rdtos,
            "user"      : user,
            }
        return HttpResponse(template.render( context, request ) )
    
# 리뷰 작성 폼
class RevwriteView( View ):
    @method_decorator( csrf_exempt )
    def dispatch(self, request, *args, **kwargs):
        return View.dispatch(self, request, *args, **kwargs)
    def get(self, request ):
        template = loader.get_template( "md_review/revwrite.html" )
        
        memid = request.session.get("memid")
        gid = request.session.get("gid")
        
        #주문id
        ordr_id = request.GET["ordr_id"]        # 28
        ordr_id = int(ordr_id)
        # logger.debug(f' ordr_id  : { ordr_id }')
        
        pagenum = request.GET["pagenum"]
        number = request.GET["number"]
        
        # 닉네임
        nick = MdUser.objects.get(user_id = memid )
        
        # 주문 내역 > 주문 메뉴명& 개수
        md_ordr_m = MdOrdrM.objects.filter(ordr_id = ordr_id)
        
        stor_m_id   = 0
        m_name      = 0
        ordr_num    = 0
        
        for mom in md_ordr_m :
            stor_m_id   = mom.stor_m_id
            ordr_num    = mom.ordr_num
            
        m_name = MdStorM.objects.filter(stor_m_id = stor_m_id)

        for mn in m_name :
            m_name = mn.stor_m_name
        
        # 태그 값 불러오기
        md_tag0 = MdTag.objects.filter(tag_g_id=0)
        md_tag1 = MdTag.objects.filter(tag_g_id=1)
        
        context = {
            "memid"     : memid,
            "gid"       : gid,
            "nick"      : nick,
            "md_ordr_m" : md_ordr_m,
            "m_name"    : m_name,
            "ordr_num"  : ordr_num,
            "md_tag0"   : md_tag0,
            "md_tag1"   : md_tag1,
            "ordr_id"  : ordr_id,
            
            }
        return HttpResponse(template.render( context, request ) )
    
    def post(self, request):
        
        rev_star    = request.POST["rev_star"]
        rev_star    = rev_star
        ordr_id     =  request.POST.get("ordr_id","")
        
        md_tag0     = request.POST.get("md_tag0","")
        md_tag1     = request.POST.getlist("md_tag1","")

        # 리뷰 저장
        rev = MdReview(
            ordr_id     = ordr_id,
            rev_star    = rev_star,
            rev_ts      = datetime.now(),
            rev_cont    = request.POST["rev_cont"],
            rev_img     = request.FILES.get("rev_img"),
            )
        rev.save()
        
        # 태그 저장
        # 리뷰 id 
        md_review = MdReview.objects.get(ordr_id = ordr_id) 
        
        rev_id = 0
        tag_id = 0
        
        rev_id = md_review.rev_id
        
        
        if md_tag0 != None :
            tag0 = MdRevT(
                rev_id = rev_id,
                tag_id = tag_id
                )
            tag0.save()
            
        if md_tag1 != None :
            for tag1 in md_tag1 :
                logger.debug(f' tag1  : { tag1 }')
                tag_id = tag1
                
                tag1 = MdRevT(
                    rev_id = rev_id,
                    tag_id = tag_id
                    )
                tag1.save()
        
        return redirect("/md_member/myorderlist")
    
