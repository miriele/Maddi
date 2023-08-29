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
from django.db.models import F

# 로그
logger = logging.getLogger( __name__ )


# 리뷰 보기 폼>매뉴 정보페이지에 합체
class ReviewView( View ):
    def get(self, request ):
        template = loader.get_template( "md_review/review.html" )   
        
        memid   = request.session.get("memid")
        gid     = request.session.get("gid")
        
        stor_id = request.GET["stor_id"]
        
        stor_id = int(stor_id)
        
        count   = 0
        #리뷰가 있나 없나 확인용
        rev_count   = MdReview.objects.select_related('ordr__mdordrm__stor_m').filter(ordr__mdordrm__stor_m__stor_id = stor_id).count()      #나옴
        # logger.debug(f' rev_count  : { rev_count }')
        
        if rev_count != 0:
            count = rev_count
        else :
            count = count
        
        # 리뷰 내용 출력 
        rdtos   = MdReview.objects.select_related('ordr__mdordrm__stor_m__stor__user').values(
            'rev_id','ordr__user__user_id', 'ordr_id', 'ordr__mdordrm__stor_m__stor__stor_name',
            'ordr__mdordrm__stor_m__stor_id', 'rev_ts', 'ordr__user__user_nick', "ordr__user__user_img",
            'rev_cont', 'rev_star', 'rev_img').annotate(
                                                re_id = F('rev_id'),
                                                user_id = F('ordr__user__user_id'),
                                                order_id = F('ordr_id'),
                                                stor_name = F('ordr__mdordrm__stor_m__stor__stor_name'),
                                                stor_id = F('ordr__mdordrm__stor_m__stor_id'),
                                                re_ts = F('rev_ts'),
                                                user_nick = F('ordr__user__user_nick'),
                                                user_img = F('ordr__user__user_img'),
                                                re_cont = F('rev_cont'),
                                                re_star = F('rev_star'),
                                                re_img = F('rev_img'),
                                                )
        # logger.debug(f' rdtos  : { rdtos }')
        
        rev_list = dict()
        
        for r in rdtos :
            re_id = r["re_id"]
            
            if re_id not in rev_list :
                rev_list[re_id]={
                    "user_id"   : r["user_id"],
                    "order_id"  : r["order_id"],
                    "stor_name" : r["stor_name"],
                    "stor_id"   : r["stor_id"],
                    "re_ts"     : r["re_ts"],
                    "user_nick" : r["user_nick"],
                    "user_img"  : r["user_img"],
                    "re_cont"   : r["re_cont"],
                    "re_star"   : r["re_star"],
                    "re_img"    : r["re_img"],
                    }
                
        tags    = MdRevT.objects.select_related('tag', 'rev').values('tag__tag_name', 'rev__rev_id')
        
        user    = MdOrdr.objects.select_related('user')
        # logger.debug(f' user  : { user }')
        
        context = {
            "rev_list"  : rev_list,
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

        memid = request.session.get("memid")
        gid = request.session.get("gid")
        
        #주문id
        ordr_id = request.GET["ordr_id"]        # 28
        ordr_id = int(ordr_id)
        
        pagenum = request.GET["pagenum"]
        
        template = loader.get_template( "md_review/revwrite.html" )
    
        # 닉네임
        nick = MdUser.objects.get(user_id = memid )
        
        # 주문 내역 > 주문 메뉴명& 개수
        menu = MdOrdrM.objects.select_related('stor_m').filter(ordr_id = ordr_id).values_list(
            'stor_m__stor_m_name', 'ordr_num')
        
        #리스트(튜플)로 반복문 돌려 값 가져옴
        menu = list(menu)
        
        # 태그 값 불러오기
        md_tag0 = MdTag.objects.filter(tag_g_id=0)
        md_tag1 = MdTag.objects.filter(tag_g_id=1)
        
        context = {
            "memid"     : memid,
            "gid"       : gid,
            "nick"      : nick,
            "menu"      : menu,
            "md_tag0"   : md_tag0,
            "md_tag1"   : md_tag1,
            "ordr_id"   : ordr_id,
            "pagenum"   : pagenum,
            }
        return HttpResponse(template.render( context, request ) )
    
    
    def post(self, request):
        md_tag0     = request.POST.get("md_tag0","")
        md_tag1     = request.POST.getlist("md_tag1","")
        ordr_id     = request.POST.get("ordr_id","")
        
        
        # 리뷰 저장
        rev = MdReview(
            ordr_id     = ordr_id,
            rev_star    = request.POST["rev_star"],
            rev_ts      = datetime.now(),
            rev_cont    = request.POST["rev_cont"],
            rev_img     = request.FILES.get("rev_img"),
            )
        rev.save()
        # logger.debug(f'md_tag0 : {md_tag0}')
        # logger.debug(f'md_tag1 : {md_tag1}')
        # logger.debug(f'cont : {request.POST["rev_cont"]}')
        # 태그 저장
        # 리뷰 id 
        md_review = MdReview.objects.get(ordr_id = ordr_id) 
        
        rev_id = md_review.rev_id
        
        
        if md_tag0 != None :
            tag1 = MdRevT(
                rev_id = rev_id,
                tag_id = md_tag0
                )
            tag1.save()
        
        if md_tag1 != None :
            for tag1 in md_tag1 :
                logger.debug(f' tag1  : { tag1 }')
        
                tag2 = MdRevT(
                    rev_id = rev_id,
                    tag_id = tag1
                    )
                tag2.save()
        

        return redirect("/md_member/myorderlist")
    
