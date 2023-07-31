from django.shortcuts import render, redirect
from django.views.generic.base import View
from django.http.response import HttpResponse
from django.template import loader
from md_member.models import MdUser, MdUserG, MdUIntr, MdIntrT, MdUTast, MdTastT,\
    MdUDsrt, MdUDrnk
from md_review.models import MdReview, MdTag, MdRevT
from md_order.models import MdOrdr, MdOrdrM
from md_store.models import MdStorReg, MdStorM, MdStorT, MdStor, MdDsrtT,\
    MdDrnkT
import logging
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.utils.dateformat import DateFormat
from datetime import datetime
from django.db.models.aggregates import Count
from django.db.models.expressions import Case
from _datetime import date
from django.db.models.functions.text import Substr
import collections
from md_admin.models import MdSrch
import json
from _collections import defaultdict





# 로그
logger = logging.getLogger( __name__ )

# 회원정보리스트
class UserlistView(View):
    def get(self,request):
        template = loader.get_template("md_admin/userlist.html")
        count = MdUser.objects.count() #회원수  
        users = MdUser.objects.select_related("user_g").only("user_id","user_name","user_g__user_g_name","user_reg_ts").order_by("-user_reg_ts") #회원리스트
        context ={
            "count":count,
            "users":users,
            }
        return HttpResponse(template.render(context,request))
    
# 회원상세정보
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
# 회원등급수정
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

# 리뷰리스트
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

# 리뷰상세정보    
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
   
# 리뷰삭제 
    def post(self,request):
        rev_id = request.POST["rev_id"]
        #리뷰태그 delete
        tdto = MdRevT.objects.filter(rev=rev_id)
        tdto.delete()
        #리뷰 delete
        rdto = MdReview.objects.get(rev_id=rev_id)
        rdto.delete()
        return redirect("/md_admin/reviewlist")

# 점주등록신청 리스트          
class SregistlistView(View):
    def get(self,request):
        template = loader.get_template("md_admin/sregistlist.html")
        reglists = MdStorReg.objects.select_related("stor")
        context ={
            "reglists":reglists,
            }
        return HttpResponse(template.render(context,request))

# 점주등록신청 상세    
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
            "reg_id" : reg_id,
            "reginfo": reginfo,
            "result" : result,
            }
        return HttpResponse(template.render(context,request))
    
# 점주등록신청 승인
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

# 통계페이지

# 가입회원 성별 통계        
class GenstatisView(View):
    def get(self,request):
        template = loader.get_template("md_admin/genstatis.html")
        count = MdUser.objects.count()
        mancount = MdUser.objects.filter(gen=0).count()
        womancount = MdUser.objects.filter(gen=1).count()
       
        #성별/인원수
        gend = [] # 성별이름 담을 리스트
        inwon = []   # 해당 성별 인원수 담을 리스트
        #남/여 count
        #SELECT g.gen_name ,COUNT(*) FROM md_user u 
        #JOIN md_gen g ON u.gen_id = g.gen_id GROUP BY g.gen_name;(김민우)
        gen = MdUser.objects.select_related('gen').values('gen__gen_name').annotate(Count('gen'))

        # print(gen)
        #<QuerySet [{'gen__gen_name': '남자\r', 'gen__count': 79}, {'gen__gen_name': '여자\r', 'gen__count': 61}]>
        
        #쿼리셋을 list로 만듦
        gen_list = list(gen)
        
        # print(gen_list)
        #[{'gen__gen_name': '남자\r', 'gen__count': 79}, 
        #{'gen__gen_name': '여자\r', 'gen__count': 61}]
        
        #key-value 리스트화
        #1.성별 key
        genname = list(m['gen__gen_name'] for m in gen_list)
        #1-1 \r제거
        genname = [l.strip() for l in genname]
        #2.성별인원수 value 리스트화
        gencount = list(m['gen__count'] for m in gen_list)
        
        #labels,data리스트에 담기
        gend.extend(genname)
        inwon.extend(gencount)
        
        # print(gend)
        # print(inwon)    

        #남성회원 비율
        menper = inwon[0]/sum(inwon) * 100
        menper = round(menper,2)
        # print(menper)
        #여성회원 비율
        womenper = inwon[1]/sum(inwon) * 100
        womenper = round(womenper,2)  
        # print(womenper)        
        
        #남성_연령대 분포
        today = datetime.today().year

        muserbir = MdUser.objects.annotate(year=Substr("user_bir",1,4)).filter(gen=0).values("year")
        man_year = list(m['year'] for m in muserbir)
        man_year = list(map(int,man_year))
        man_age = list(map(lambda x:x - today , man_year))
        man_age = list(map(abs,man_age))
                
        man_teen = list(filter(lambda x: x<20 and x >=10, man_age))
        man_twe = list(filter(lambda x: x<30 and x >=20, man_age))
        man_thr = list(filter(lambda x: x<40 and x >=30, man_age))
        man_fou = list(filter(lambda x: x<50 and x >=40, man_age))
        man_fif = list(filter(lambda x: x<60 and x >=50, man_age))
        man_older = list(filter(lambda x: x >=60, man_age))
        man_agecount = [len(man_teen),len(man_twe),len(man_thr),len(man_fou),len(man_fif),len(man_older)]        
        # print(man_agecount)
        
        #여성_연령대 분포
        wmuserbir = MdUser.objects.annotate(year=Substr("user_bir",1,4)).filter(gen=1).values("year")
        wo_year = list(m['year'] for m in wmuserbir)
        wo_year = list(map(int,wo_year))
        woman_age = list(map(lambda x:x - today , wo_year))
        woman_age = list(map(abs,woman_age))
                
        woman_teen = list(filter(lambda x: x<20 and x >=10, woman_age))
        woman_twe = list(filter(lambda x: x<30 and x >=20, woman_age))
        woman_thr = list(filter(lambda x: x<40 and x >=30, woman_age))
        woman_fou = list(filter(lambda x: x<50 and x >=40, woman_age))
        woman_fif = list(filter(lambda x: x<60 and x >=50, woman_age))
        woman_older = list(filter(lambda x: x >=60, woman_age))
        woman_agecount = [len(woman_teen),len(woman_twe),len(woman_thr),len(woman_fou),len(woman_fif),len(woman_older)]        
        # print(woman_agecount)
        
        #데이터 TEMPLATE로 넘기기
        context = {
            "inwon"     : inwon,
            "gend"      : gend,
            "menper"    : menper,
            "womenper"  : womenper,
            "count"     : count,
            "mancount"  : mancount,
            "womancount": womancount,
            "man_agecount" : man_agecount,
            "woman_agecount": woman_agecount,
            }
        return HttpResponse(template.render(context,request))
    
# 가입회원 연령 통계    
class AgestatisView(View):
    def get(self,request):
        template = loader.get_template("md_admin/agestatis.html")
        #연령대
        #오늘 날짜 구하기
        today = datetime.today().year
        # print(type(today))
        
        #유저들의 생년월일 데이터 받아오기
        count = MdUser.objects.all().count
        userbir = MdUser.objects.annotate(year=Substr("user_bir",1,4)).values("year")
        #print(userbir)
        
        #나이계산
        year = list(m['year'] for m in userbir)
        year = list(map(int,year))
        age = list(map(lambda x:x - today , year))
        age = list(map(abs,age))
        
        #10대 인원수
        teen = list(filter(lambda x: x<20 and x >=10, age))
        # print(teen)
        
        #20대 인원수
        twe = list(filter(lambda x: x<30 and x >=20, age))
        # print(twe)
        
        #30대 인원수
        thr = list(filter(lambda x: x<40 and x >=30, age))
        # print(thr)
        
        #40대 인원수
        fou = list(filter(lambda x: x<50 and x >=40, age))
        # print(fou)
        
        #50대 인원수   
        fif = list(filter(lambda x: x<60 and x >=50, age))
        # print(fif)
        
        #60대이상 인원수
        older = list(filter(lambda x: x >=60, age))
        # print(older)
        agecount = [len(teen),len(twe),len(thr),len(fou),len(fif),len(older)]
   
        # print(age)
        # print(year)
        context = {
            "agecount"  : agecount,
            "count"     : count,
            }
        return HttpResponse(template.render(context,request))

# 가입회원 관심사 통계    
class IntereView(View):
    def get(self,request):
        template = loader.get_template("md_admin/interestatis.html")
        # 전체 회원들의 관심사 전체 고른 수
        today = datetime.today().year
        count = MdUIntr.objects.all().count()
        inter = MdUIntr.objects.values("intr_t").order_by("intr_t")
        inter_name = MdIntrT.objects.values("intr_t_name").order_by("intr_t_id")
        # print(inter)
        inter = list(m['intr_t'] for m in inter)
        
        inter_name = list(m['intr_t_name'] for m in inter_name)
        inter_name = [l.strip() for l in inter_name]
        
        #뽑아온 리스트를 key값순으로 sort하기위해 dict 생성
        dict_inter = {}
        dict_inter = collections.Counter(inter)
        #sort한 key들을 다시 리스트로 넣기
        list_inter = []
        for key,value in sorted(dict_inter.items()):
            list_inter.append(value)
        # print(len(list_inter))
        # 남성회원들의 관심사
        maninter = MdUIntr.objects.annotate(year= Substr("user__user_bir",1,4)).filter(user__gen=0).values_list("intr_t","year").order_by("intr_t")
        # print(maninter)
        
        maninter_list = list(maninter)
        up_agelist = []
        up_interlist = []
        # print(maninter)
        # print(type(maninter_list[0][1]))
        for myear in maninter_list:
            minter = myear[0]
            myear = int(myear[1])
            age = today - myear
            #print(age)
            if(age >=10 and age<20):
                age = '10대'
            elif(age>=20 and age<30):
                age = '20대'
            elif(age>=30 and age<40):
                age = '30대'
            elif(age>=40 and age<50):
                age = '40대'
            elif(age>=50 and age<60):
                age = '50대'
            else:
                age = '60대이상'
            up_agelist.append(age)
            up_interlist.append(minter)
        
        #print(len(up_agelist))
        #print(len(up_interlist))
        
        ziptup = list(zip(up_agelist,up_interlist))
        #print(ziptup)
        
        ziplist = [list(row) for row in ziptup]
        # print(ziplist)
        
        teen_manlist = [i[1] for i in ziplist if i[0]=='10대']
        twe_manlist = [i[1] for i in ziplist if i[0]=='20대']
        thr_manlist = [i[1] for i in ziplist if i[0]=='30대']
        fou_manlist = [i[1] for i in ziplist if i[0]=='40대']
        fiv_manlist = [i[1] for i in ziplist if i[0]=='50대']
        ord_manlist = [i[1] for i in ziplist if i[0]=='60대이상']
        
        manteen_dict = collections.Counter(teen_manlist)
        mantwe_dict = collections.Counter(twe_manlist)
        manthr_dict = collections.Counter(thr_manlist)
        manfou_dict = collections.Counter(fou_manlist)
        manfiv_dict = collections.Counter(fiv_manlist)
        manord_dict = collections.Counter(ord_manlist)
        
        
        manteen_list = []
        mantwe_list = []
        manthr_list = []
        manfou_list = []
        manfiv_list = []
        manord_list = []
        for i in range(len(inter_name)):
            manteen_list.append(0)
            mantwe_list.append(0)
            manthr_list.append(0)
            manfou_list.append(0)
            manfiv_list.append(0)
            manord_list.append(0)
        # print(manteen_list)
        
        for key,value in sorted(manteen_dict.items()):
            for index,val in enumerate(manteen_list):
                manteen_list[key] = value

        for key,value in sorted(mantwe_dict.items()):
            for index,val in enumerate(mantwe_list):
                mantwe_list[key] = value

        for key,value in sorted(manthr_dict.items()):
            for index,val in enumerate(manthr_list):
                manthr_list[key] = value

        for key,value in sorted(manfou_dict.items()):
            for index,val in enumerate(manfou_list):
                manfou_list[key] = value                                        

        for key,value in sorted(manfiv_dict.items()):
            for index,val in enumerate(manfiv_list):
                manfiv_list[key] = value
                
        for key,value in sorted(manord_dict.items()):
            for index,val in enumerate(manord_list):
                manord_list[key] = value                

# 여성회원들의 관심사
        womaninter = MdUIntr.objects.annotate(year= Substr("user__user_bir",1,4)).filter(user__gen=1).values_list("intr_t","year").order_by("intr_t")
        womaninter_list = list(womaninter)
        #print(womaninter)
        wup_agelist = []
        wup_interlist = []
        
        for wmyear in womaninter_list:
            womaninter = wmyear[0]
            wmyear = int(wmyear[1])
            womanage = today - wmyear
            if(womanage >=10 and womanage<20):
                womanage = '10대'
            elif(womanage>=20 and womanage<30):
                womanage = '20대'
            elif(womanage>=30 and womanage<40):
                womanage = '30대'
            elif(womanage>=40 and womanage<50):
                womanage = '40대'
            elif(womanage>=50 and womanage<60):
                womanage = '50대'
            else:
                womanage = '60대이상'
            wup_agelist.append(womanage)
            wup_interlist.append(womaninter)
        # print(up_agelist)
        # print(up_interlist)
        
        wziptup = list(zip(wup_agelist,wup_interlist))
        #print(ziptup)
        
        wziplist = [list(row) for row in wziptup]
        # print(wziplist)
        
        teen_womanlist = [i[1] for i in wziplist if i[0]=='10대']
        twe_womanlist = [i[1] for i in wziplist if i[0]=='20대']
        thr_womanlist = [i[1] for i in wziplist if i[0]=='30대']
        fou_womanlist = [i[1] for i in wziplist if i[0]=='40대']
        fiv_womanlist = [i[1] for i in wziplist if i[0]=='50대']
        ord_womanlist = [i[1] for i in wziplist if i[0]=='60대이상']
        
        womanteen_dict = collections.Counter(teen_womanlist)
        womantwe_dict = collections.Counter(twe_womanlist)
        womanthr_dict = collections.Counter(thr_womanlist)
        womanfou_dict = collections.Counter(fou_womanlist)
        womanfiv_dict = collections.Counter(fiv_womanlist)
        womanord_dict = collections.Counter(ord_womanlist)
           
        womanteen_list = []
        womantwe_list = []
        womanthr_list = []
        womanfou_list = []
        womanfiv_list = []
        womanord_list = []
        for i in range(len(inter_name)):
            womanteen_list.append(0)
            womantwe_list.append(0)
            womanthr_list.append(0)
            womanfou_list.append(0)
            womanfiv_list.append(0)
            womanord_list.append(0) 
        
        for key,value in sorted(womanteen_dict.items()):
            for index,val in enumerate(womanteen_list):
                womanteen_list[key] = value

        for key,value in sorted(womantwe_dict.items()):
            for index,val in enumerate(womantwe_list):
                womantwe_list[key] = value

        for key,value in sorted(womanthr_dict.items()):
            for index,val in enumerate(womanthr_list):
                womanthr_list[key] = value

        for key,value in sorted(womanfou_dict.items()):
            for index,val in enumerate(womanfou_list):
                womanfou_list[key] = value                                        

        for key,value in sorted(womanfiv_dict.items()):
            for index,val in enumerate(womanfiv_list):
                womanfiv_list[key] = value
                
        for key,value in sorted(womanord_dict.items()):
            for index,val in enumerate(womanord_list):
                womanord_list[key] = value                
       
        context = {
            "list_inter": list_inter,
            "inter_name": inter_name,
            "manteen_list": manteen_list,
            "mantwe_list" : mantwe_list,
            "manthr_list" : manthr_list,
            "manfou_list" : manfou_list,
            "manfiv_list" : manfiv_list,
            "manord_list" : manord_list,
            "womanteen_list": womanteen_list,
            "womantwe_list" : womantwe_list,
            "womanthr_list" : womanthr_list,
            "womanfou_list" : womanfou_list,
            "womanfiv_list" : womanfiv_list,
            "womanord_list" : womanord_list,            
            }
        return HttpResponse(template.render(context,request))

# 가입회원 입맛 통계
class TasteView(View):
    def get(self,request):
        template = loader.get_template("md_admin/tastestatis.html")
        today = datetime.today().year
        #입맛 전체 회원 id지정 수
        tast = MdUTast.objects.values("tast_t").order_by("tast_t")
        tast = list(m['tast_t'] for m in tast)
        
        dict_tast = {}
        dict_tast = collections.Counter(tast)
        list_tast = []
        for key,value in sorted(dict_tast.items()):
            list_tast.append(value)
        
        #입맛 이름
        tast_n = MdTastT.objects.values("tast_t_name").order_by("tast_t_id")
        tast_n = list(m['tast_t_name'] for m in tast_n)
        #print(tast_n)
        
        #남성 회원 입맛
        mantast = MdUTast.objects.annotate(year= Substr("user__user_bir",1,4)).filter(user__gen=0).values_list("tast_t","year").order_by("tast_t")
        mantast_list = list(mantast)
        
        up_agelist = []
        up_tastlist = []
        
        for myear in mantast_list:
            mtast = myear[0]
            myear = int(myear[1])
            age = today - myear
            #print(age)
            if(age >=10 and age<20):
                age = '10대'
            elif(age>=20 and age<30):
                age = '20대'
            elif(age>=30 and age<40):
                age = '30대'
            elif(age>=40 and age<50):
                age = '40대'
            elif(age>=50 and age<60):
                age = '50대'
            else:
                age = '60대이상'
            up_agelist.append(age)
            up_tastlist.append(mtast)

        ziptup = list(zip(up_agelist,up_tastlist))
        #print(ziptup)
        
        ziplist = [list(row) for row in ziptup]
        # print(ziplist)
        
        teen_manlist = [i[1] for i in ziplist if i[0]=='10대']
        twe_manlist = [i[1] for i in ziplist if i[0]=='20대']
        thr_manlist = [i[1] for i in ziplist if i[0]=='30대']
        fou_manlist = [i[1] for i in ziplist if i[0]=='40대']
        fiv_manlist = [i[1] for i in ziplist if i[0]=='50대']
        ord_manlist = [i[1] for i in ziplist if i[0]=='60대이상']
        
        manteen_dict = collections.Counter(teen_manlist)
        mantwe_dict = collections.Counter(twe_manlist)
        manthr_dict = collections.Counter(thr_manlist)
        manfou_dict = collections.Counter(fou_manlist)
        manfiv_dict = collections.Counter(fiv_manlist)
        manord_dict = collections.Counter(ord_manlist)        
        
        manteen_tlist = []
        mantwe_tlist = []
        manthr_tlist = []
        manfou_tlist = []
        manfiv_tlist = []
        manord_tlist = []
        for i in range(len(tast_n)):
            manteen_tlist.append(0)
            mantwe_tlist.append(0)
            manthr_tlist.append(0)
            manfou_tlist.append(0)
            manfiv_tlist.append(0)
            manord_tlist.append(0)
        # print(manteen_list)
 
        for key,value in sorted(manteen_dict.items()):
            for index,val in enumerate(manteen_tlist):
                manteen_tlist[key] = value
    
        for key,value in sorted(mantwe_dict.items()):
            for index,val in enumerate(mantwe_tlist):
                mantwe_tlist[key] = value
    
        for key,value in sorted(manthr_dict.items()):
            for index,val in enumerate(manthr_tlist):
                manthr_tlist[key] = value
    
        for key,value in sorted(manfou_dict.items()):
            for index,val in enumerate(manfou_tlist):
                manfou_tlist[key] = value                                        
    
        for key,value in sorted(manfiv_dict.items()):
            for index,val in enumerate(manfiv_tlist):
                manfiv_tlist[key] = value
                
        for key,value in sorted(manord_dict.items()):
            for index,val in enumerate(manord_tlist):
                manord_tlist[key] = value         
 
        #여성 회원 입맛
        wmantast = MdUTast.objects.annotate(year= Substr("user__user_bir",1,4)).filter(user__gen=1).values_list("tast_t","year").order_by("tast_t")
        wmantast_list = list(wmantast)
        
        wup_agelist = []
        wup_tastlist = []
        
        for wyear in wmantast_list:
            wtast = wyear[0]
            wyear = int(wyear[1])
            womanage = today - wyear
            #print(age)
            if(womanage >=10 and womanage<20):
                womanage = '10대'
            elif(womanage>=20 and womanage<30):
                womanage = '20대'
            elif(womanage>=30 and womanage<40):
                womanage = '30대'
            elif(womanage>=40 and womanage<50):
                womanage = '40대'
            elif(womanage>=50 and womanage<60):
                womanage = '50대'
            else:
                womanage = '60대이상'
            wup_agelist.append(womanage)
            wup_tastlist.append(wtast)

        wziptup = list(zip(wup_agelist,wup_tastlist))
        #print(ziptup)
        
        wziplist = [list(row) for row in wziptup]
        # print(ziplist)
        
        teen_womanlist = [i[1] for i in wziplist if i[0]=='10대']
        twe_womanlist = [i[1] for i in wziplist if i[0]=='20대']
        thr_womanlist = [i[1] for i in wziplist if i[0]=='30대']
        fou_womanlist = [i[1] for i in wziplist if i[0]=='40대']
        fiv_womanlist = [i[1] for i in wziplist if i[0]=='50대']
        ord_womanlist = [i[1] for i in wziplist if i[0]=='60대이상']
        
        womanteen_dict = collections.Counter(teen_womanlist)
        womantwe_dict = collections.Counter(twe_womanlist)
        womanthr_dict = collections.Counter(thr_womanlist)
        womanfou_dict = collections.Counter(fou_womanlist)
        womanfiv_dict = collections.Counter(fiv_womanlist)
        womanord_dict = collections.Counter(ord_womanlist)        
        
        womanteen_tlist = []
        womantwe_tlist = []
        womanthr_tlist = []
        womanfou_tlist = []
        womanfiv_tlist = []
        womanord_tlist = []
        for i in range(len(tast_n)):
            womanteen_tlist.append(0)
            womantwe_tlist.append(0)
            womanthr_tlist.append(0)
            womanfou_tlist.append(0)
            womanfiv_tlist.append(0)
            womanord_tlist.append(0)
        # print(manteen_list)
 
        for key,value in sorted(womanteen_dict.items()):
            for index,val in enumerate(womanteen_tlist):
                womanteen_tlist[key] = value
    
        for key,value in sorted(womantwe_dict.items()):
            for index,val in enumerate(womantwe_tlist):
                womantwe_tlist[key] = value
    
        for key,value in sorted(womanthr_dict.items()):
            for index,val in enumerate(womanthr_tlist):
                womanthr_tlist[key] = value
    
        for key,value in sorted(womanfou_dict.items()):
            for index,val in enumerate(womanfou_tlist):
                womanfou_tlist[key] = value                                        
    
        for key,value in sorted(womanfiv_dict.items()):
            for index,val in enumerate(womanfiv_tlist):
                womanfiv_tlist[key] = value
                
        for key,value in sorted(womanord_dict.items()):
            for index,val in enumerate(womanord_tlist):
                womanord_tlist[key] = value     
               
        context = {
            "list_tast": list_tast,
            "tast_n"   : tast_n,
            "manteen_tlist" : manteen_tlist,
            "mantwe_tlist" : mantwe_tlist,
            "manthr_tlist" : manthr_tlist,
            "manfou_tlist" : manfou_tlist,
            "manfiv_tlist" : manfiv_tlist,
            "manord_tlist" : manord_tlist,
            "womanteen_tlist" : womanteen_tlist,
            "womantwe_tlist" : womantwe_tlist,
            "womanthr_tlist" : womanthr_tlist,
            "womanfou_tlist" : womanfou_tlist,
            "womanfiv_tlist" : womanfiv_tlist,
            "womanord_tlist" : womanord_tlist,            
            }
        return HttpResponse(template.render(context,request))

# 사이트 매장등록 통계
class StoreView(View):
    def get(self,request):
        template = loader.get_template("md_admin/storestatis.html")
        scount = MdStor.objects.all().count()
        
        #매장구분 개인/프랜차이즈
        pstor = MdStor.objects.filter(stor_t=0).count()
        fstor = MdStor.objects.exclude(stor_t=0).count()

        #개인매장등록일
        # pregstor = MdStorReg.objects.select_related("stor").filter(stor__stor_t=0 , reg_con_ts__isnull = False).values("reg_con_ts")
        # #프랜차이즈매장등록일
        # fregstor = MdStorReg.objects.select_related("stor").exclude(stor__stor_t=0 , reg_con_ts = None).values("reg_con_ts")
        # print(str(fregstor.query))
        # print(pregstor)
        # print(fregstor)
        
        stor_list = [pstor,fstor]
        
        context = {
            "scount" : scount,
            "stor_list" : stor_list, 
            }
        return HttpResponse(template.render(context,request))

# 가입회원 디저트 취향    
class DsrtView(View):
    def get(self,request):
        template = loader.get_template("md_admin/dsrtstatis.html")
        today = datetime.today().year
        #사용자 디저트 기입한 수 리스트
        dsrt = MdUDsrt.objects.values("dsrt_t").order_by("dsrt_t")
        dsrt = list(m['dsrt_t'] for m in dsrt)
        dict_dsrt = {}
        dict_dsrt = collections.Counter(dsrt)
        list_dsrt = []
        for key,value in sorted(dict_dsrt.items()):
            list_dsrt.append(value)
        # print(list_dsrt)
        
        #디저트분류명 리스트
        dsrt_n = MdDsrtT.objects.values("dsrt_t_name")
        dsrt_n = list(m['dsrt_t_name'] for m in dsrt_n)
        
        
        # print(dsrt_n)
                     
        #남성회원 디저트 취향
        mandsrt = MdUDsrt.objects.annotate(year= Substr("user__user_bir",1,4)).filter(user__gen=0).values_list("dsrt_t","year").order_by("dsrt_t")
        mandsrt_list = list(mandsrt)
        
        up_agelist = []
        up_dsrtlist = []
        
        for myear in mandsrt_list:
            mdsrt = myear[0]
            myear = int(myear[1])
            age = today - myear
            #print(age)
            if(age >=10 and age<20):
                age = '10대'
            elif(age>=20 and age<30):
                age = '20대'
            elif(age>=30 and age<40):
                age = '30대'
            elif(age>=40 and age<50):
                age = '40대'
            elif(age>=50 and age<60):
                age = '50대'
            else:
                age = '60대이상'
            up_agelist.append(age)
            up_dsrtlist.append(mdsrt)

        ziptup = list(zip(up_agelist,up_dsrtlist))
        #print(ziptup)
        
        ziplist = [list(row) for row in ziptup]
        # print(ziplist)
        
        teen_manlist = [i[1] for i in ziplist if i[0]=='10대']
        twe_manlist = [i[1] for i in ziplist if i[0]=='20대']
        thr_manlist = [i[1] for i in ziplist if i[0]=='30대']
        fou_manlist = [i[1] for i in ziplist if i[0]=='40대']
        fiv_manlist = [i[1] for i in ziplist if i[0]=='50대']
        ord_manlist = [i[1] for i in ziplist if i[0]=='60대이상']
        # print(teen_manlist)
        
        manteen_dict = collections.Counter(teen_manlist)
        mantwe_dict = collections.Counter(twe_manlist)
        manthr_dict = collections.Counter(thr_manlist)
        manfou_dict = collections.Counter(fou_manlist)
        manfiv_dict = collections.Counter(fiv_manlist)
        manord_dict = collections.Counter(ord_manlist)        
        
        manteen_dslist = []
        mantwe_dslist = []
        manthr_dslist = []
        manfou_dslist = []
        manfiv_dslist = []
        manord_dslist = []
        for i in range(len(dsrt_n)-1):
            manteen_dslist.append(0)
            mantwe_dslist.append(0)
            manthr_dslist.append(0)
            manfou_dslist.append(0)
            manfiv_dslist.append(0)
            manord_dslist.append(0)
        # print(manteen_list)
 
        for key,value in sorted(manteen_dict.items()):
            for index,val in enumerate(manteen_dslist):
                manteen_dslist[key] = value
    
        for key,value in sorted(mantwe_dict.items()):
            for index,val in enumerate(mantwe_dslist):
                mantwe_dslist[key] = value
    
        for key,value in sorted(manthr_dict.items()):
            for index,val in enumerate(manthr_dslist):
                manthr_dslist[key] = value
    
        for key,value in sorted(manfou_dict.items()):
            for index,val in enumerate(manfou_dslist):
                manfou_dslist[key] = value                                        
    
        for key,value in sorted(manfiv_dict.items()):
            for index,val in enumerate(manfiv_dslist):
                manfiv_dslist[key] = value
                
        for key,value in sorted(manord_dict.items()):
            for index,val in enumerate(manord_dslist):
                manord_dslist[key] = value                 
        
        #여성 디저트 취향
        womandsrt = MdUDsrt.objects.annotate(year= Substr("user__user_bir",1,4)).filter(user__gen=1).values_list("dsrt_t","year").order_by("dsrt_t")
        womandsrt_list = list(womandsrt)
        
        wup_agelist = []
        wup_dsrtlist = []
        
        for wmyear in womandsrt_list:
            wmdsrt = wmyear[0]
            wmyear = int(wmyear[1])
            wage = today - wmyear
            #print(age)
            if(wage >=10 and wage<20):
                wage = '10대'
            elif(wage>=20 and wage<30):
                wage = '20대'
            elif(wage>=30 and wage<40):
                wage = '30대'
            elif(wage>=40 and wage<50):
                wage = '40대'
            elif(wage>=50 and wage<60):
                wage = '50대'
            else:
                wage = '60대이상'
            wup_agelist.append(wage)
            wup_dsrtlist.append(wmdsrt)

        wziptup = list(zip(wup_agelist,wup_dsrtlist))
        #print(ziptup)
        
        wziplist = [list(row) for row in wziptup]
        # print(ziplist)
        
        teen_womanlist = [i[1] for i in wziplist if i[0]=='10대']
        twe_womanlist = [i[1] for i in wziplist if i[0]=='20대']
        thr_womanlist = [i[1] for i in wziplist if i[0]=='30대']
        fou_womanlist = [i[1] for i in wziplist if i[0]=='40대']
        fiv_womanlist = [i[1] for i in wziplist if i[0]=='50대']
        ord_womanlist = [i[1] for i in wziplist if i[0]=='60대이상']
        # print(teen_manlist)
        
        womanteen_dict = collections.Counter(teen_womanlist)
        womantwe_dict = collections.Counter(twe_womanlist)
        womanthr_dict = collections.Counter(thr_womanlist)
        womanfou_dict = collections.Counter(fou_womanlist)
        womanfiv_dict = collections.Counter(fiv_womanlist)
        womanord_dict = collections.Counter(ord_womanlist)        
        
        womanteen_dslist = []
        womantwe_dslist = []
        womanthr_dslist = []
        womanfou_dslist = []
        womanfiv_dslist = []
        womanord_dslist = []
        for i in range(len(dsrt_n)-1):
            womanteen_dslist.append(0)
            womantwe_dslist.append(0)
            womanthr_dslist.append(0)
            womanfou_dslist.append(0)
            womanfiv_dslist.append(0)
            womanord_dslist.append(0)
        # print(manteen_list)
 
        for key,value in sorted(womanteen_dict.items()):
            for index,val in enumerate(womanteen_dslist):
                womanteen_dslist[key] = value
    
        for key,value in sorted(womantwe_dict.items()):
            for index,val in enumerate(womantwe_dslist):
                womantwe_dslist[key] = value
    
        for key,value in sorted(womanthr_dict.items()):
            for index,val in enumerate(womanthr_dslist):
                womanthr_dslist[key] = value
    
        for key,value in sorted(womanfou_dict.items()):
            for index,val in enumerate(womanfou_dslist):
                womanfou_dslist[key] = value                                        
    
        for key,value in sorted(womanfiv_dict.items()):
            for index,val in enumerate(womanfiv_dslist):
                womanfiv_dslist[key] = value
                
        for key,value in sorted(womanord_dict.items()):
            for index,val in enumerate(womanord_dslist):
                womanord_dslist[key] = value            
        # print(len(manteen_dslist))
        # 디저트 분류 리스트 '없음' 제거
        dsrt_n.remove('없음' )
        # print(dsrt_n)
        
        context = {
            "dsrt_n" : dsrt_n,
            "list_dsrt" : list_dsrt,
            "manteen_dslist" : manteen_dslist,
            "mantwe_dslist" : mantwe_dslist,
            "manthr_dslist" : manthr_dslist,
            "manfou_dslist" : manfou_dslist,
            "manfiv_dslist" : manfiv_dslist,
            "manord_dslist" : manord_dslist,
            "womanteen_dslist" : womanteen_dslist,
            "womantwe_dslist" : womantwe_dslist,
            "womanthr_dslist" : womanthr_dslist,
            "womanfou_dslist" : womanfou_dslist,
            "womanfiv_dslist" : womanfiv_dslist,
            "womanord_dslist" : womanord_dslist,            
            }
        return HttpResponse(template.render(context,request))
    
# 가입회원 음료 취향
class DrnkView(View):
    def get(self,request):
        template = loader.get_template("md_admin/drnkstatis.html")
        today = datetime.today().year
        #사용자 음료 기입한 수 리스트
        drnk = MdUDrnk.objects.values("drnk_t").order_by("drnk_t")
        drnk = list(m['drnk_t'] for m in drnk)
        
        dict_drnk = {}
        dict_drnk = collections.Counter(drnk)
        list_drnk = []
        for key,value in sorted(dict_drnk.items()):
            list_drnk.append(value)
        # print(list_drnk)
        
        #음료분류명 리스트
        drnk_n = MdDrnkT.objects.values("drnk_t_name")
        drnk_n = list(m['drnk_t_name'] for m in drnk_n)
        
         
        #남성회원 음료취향
        mandrnk = MdUDrnk.objects.annotate(year= Substr("user__user_bir",1,4)).filter(user__gen=0).values_list("drnk_t","year").order_by("drnk_t")
        mandrnk_list = list(mandrnk)
        
        up_agelist = []
        up_drnklist = []
        
        for myear in mandrnk_list:
            mdrnk = myear[0]
            myear = int(myear[1])
            age = today - myear
            #print(age)
            if(age >=10 and age<20):
                age = '10대'
            elif(age>=20 and age<30):
                age = '20대'
            elif(age>=30 and age<40):
                age = '30대'
            elif(age>=40 and age<50):
                age = '40대'
            elif(age>=50 and age<60):
                age = '50대'
            else:
                age = '60대이상'
            up_agelist.append(age)         
            up_drnklist.append(mdrnk)
            
        ziptup = list(zip(up_agelist,up_drnklist))
        ziplist = [list(row) for row in ziptup]
        
        teen_manlist = [i[1] for i in ziplist if i[0]=='10대']
        twe_manlist = [i[1] for i in ziplist if i[0]=='20대']
        thr_manlist = [i[1] for i in ziplist if i[0]=='30대']
        fou_manlist = [i[1] for i in ziplist if i[0]=='40대']
        fiv_manlist = [i[1] for i in ziplist if i[0]=='50대']
        ord_manlist = [i[1] for i in ziplist if i[0]=='60대이상']
        
        manteen_drnk = collections.Counter(teen_manlist)
        mantwe_drnk = collections.Counter(twe_manlist)
        manthr_drnk = collections.Counter(thr_manlist)
        manfou_drnk = collections.Counter(fou_manlist)
        manfiv_drnk = collections.Counter(fiv_manlist)
        manord_drnk = collections.Counter(ord_manlist)        
        
        manteen_drlist = []
        mantwe_drlist = []
        manthr_drlist = []
        manfou_drlist = []
        manfiv_drlist = []
        manord_drlist = []
        
        for i in range(len(drnk_n)-1):
            manteen_drlist.append(0)
            mantwe_drlist.append(0)
            manthr_drlist.append(0)
            manfou_drlist.append(0)
            manfiv_drlist.append(0)
            manord_drlist.append(0)
 
        for key,value in sorted(manteen_drnk.items()):
            for index,val in enumerate(manteen_drlist):
                manteen_drlist[key] = value
    
        for key,value in sorted(mantwe_drnk.items()):
            for index,val in enumerate(mantwe_drlist):
                mantwe_drlist[key] = value
    
        for key,value in sorted(manthr_drnk.items()):
            for index,val in enumerate(manthr_drlist):
                manthr_drlist[key] = value
    
        for key,value in sorted(manfou_drnk.items()):
            for index,val in enumerate(manfou_drlist):
                manfou_drlist[key] = value                                        
    
        for key,value in sorted(manfiv_drnk.items()):
            for index,val in enumerate(manfiv_drlist):
                manfiv_drlist[key] = value
                
        for key,value in sorted(manord_drnk.items()):
            for index,val in enumerate(manord_drlist):
                manord_drlist[key] = value
                    
        #여성 음료 취향
        womandrnk = MdUDrnk.objects.annotate(year= Substr("user__user_bir",1,4)).filter(user__gen=1).values_list("drnk_t","year").order_by("drnk_t")
        womandrnk_list = list(womandrnk)
        
        wup_agelist = []
        wup_drnklist = []
        
        for wmyear in womandrnk_list:
            wmdrnk = wmyear[0]
            wmyear = int(wmyear[1])
            wage = today - wmyear
            #print(age)
            if(wage >=10 and wage<20):
                wage = '10대'
            elif(wage>=20 and wage<30):
                wage = '20대'
            elif(wage>=30 and wage<40):
                wage = '30대'
            elif(wage>=40 and wage<50):
                wage = '40대'
            elif(wage>=50 and wage<60):
                wage = '50대'
            else:
                wage = '60대이상'
            wup_agelist.append(wage)         
            wup_drnklist.append(wmdrnk)
            
        wziptup = list(zip(wup_agelist,wup_drnklist))  
        wziplist = [list(row) for row in wziptup]

        
        teen_womanlist = [i[1] for i in wziplist if i[0]=='10대']
        twe_womanlist = [i[1] for i in wziplist if i[0]=='20대']
        thr_womanlist = [i[1] for i in wziplist if i[0]=='30대']
        fou_womanlist = [i[1] for i in wziplist if i[0]=='40대']
        fiv_womanlist = [i[1] for i in wziplist if i[0]=='50대']
        ord_womanlist = [i[1] for i in wziplist if i[0]=='60대이상']
        
        womanteen_drnk = collections.Counter(teen_womanlist)
        womantwe_drnk = collections.Counter(twe_womanlist)
        womanthr_drnk = collections.Counter(thr_womanlist)
        womanfou_drnk = collections.Counter(fou_womanlist)
        womanfiv_drnk = collections.Counter(fiv_womanlist)
        womanord_drnk = collections.Counter(ord_womanlist)        
        
        womanteen_drlist = []
        womantwe_drlist = []
        womanthr_drlist = []
        womanfou_drlist = []
        womanfiv_drlist = []
        womanord_drlist = []
        
        for i in range(len(drnk_n)-1):
            womanteen_drlist.append(0)
            womantwe_drlist.append(0)
            womanthr_drlist.append(0)
            womanfou_drlist.append(0)
            womanfiv_drlist.append(0)
            womanord_drlist.append(0)
 
        for key,value in sorted(womanteen_drnk.items()):
            for index,val in enumerate(womanteen_drlist):
                womanteen_drlist[key] = value
    
        for key,value in sorted(womantwe_drnk.items()):
            for index,val in enumerate(womantwe_drlist):
                womantwe_drlist[key] = value
    
        for key,value in sorted(womanthr_drnk.items()):
            for index,val in enumerate(womanthr_drlist):
                womanthr_drlist[key] = value
    
        for key,value in sorted(womanfou_drnk.items()):
            for index,val in enumerate(womanfou_drlist):
                womanfou_drlist[key] = value                                        
    
        for key,value in sorted(womanfiv_drnk.items()):
            for index,val in enumerate(womanfiv_drlist):
                womanfiv_drlist[key] = value
                
        for key,value in sorted(womanord_drnk.items()):
            for index,val in enumerate(womanord_drlist):
                womanord_drlist[key] = value                
        
        
        # 음료 분류 리스트 '없음' 제거
        drnk_n.remove('없음')
        # print(dsrt_n)    
        context = {
            "drnk_n" : drnk_n,
            "list_drnk" : list_drnk,
            "manteen_drlist" : manteen_drlist,
            "mantwe_drlist" : mantwe_drlist,
            "manthr_drlist" : manthr_drlist,
            "manfou_drlist" : manfou_drlist,
            "manfiv_drlist" : manfiv_drlist,
            "manord_drlist" : manord_drlist,
            "womanteen_drlist" : womanteen_drlist,
            "womantwe_drlist" : womantwe_drlist,
            "womanthr_drlist" : womanthr_drlist,
            "womanfou_drlist" : womanfou_drlist,
            "womanfiv_drlist" : womanfiv_drlist,
            "womanord_drlist" : womanord_drlist,           
            }
           
        return HttpResponse(template.render(context,request))

#구매기반 음료 취향
class BdrnkView(View):
    def get(self,request):
        template = loader.get_template("md_admin/bdrnkstatis.html")
        today = datetime.today().year
        # 구매한 음료 분류 정보
        bdrnk = MdOrdrM.objects.select_related("stor_m__menu").values("stor_m__menu__drnk_t")
        bdrnk = list(m['stor_m__menu__drnk_t'] for m in bdrnk)
        # 음료분류 아이디 -1은 삭제
        bdrnk = [item for item in bdrnk if item != -1]
        dict_bdrnk = {}
        dict_bdrnk = collections.Counter(bdrnk)   
        # 음료분류명
        bdrnk_n = MdDrnkT.objects.values("drnk_t_name").order_by("drnk_t_id")
        bdrnk_n = list(m['drnk_t_name'] for m in bdrnk_n)
        bdrnk_n.remove('없음')
        
        bdrnk_list = []
        for i in range(len(bdrnk_n)):
            bdrnk_list.append(0)
        
        for key,value in sorted(dict_bdrnk.items()):
            for index,val in enumerate(bdrnk_list):
                bdrnk_list[key] = value
        
         
        # 남성 구매기반 음료 취향        
        mbdrnk = MdOrdrM.objects.annotate(year = Substr("ordr__user__user_bir",1,4)).select_related("stor_m__menu").filter(ordr__user__gen=0).values_list("stor_m__menu__drnk_t","year")
        mbdrnk_list = list(mbdrnk)
         
        up_agelist = []
        up_bdrnklist = []
        
        for myear in mbdrnk_list:
            mbdrnk = myear[0]
            myear = int(myear[1])
            age = today - myear
            #print(age)
            if(age >=10 and age<20):
                age = '10대'
            elif(age>=20 and age<30):
                age = '20대'
            elif(age>=30 and age<40):
                age = '30대'
            elif(age>=40 and age<50):
                age = '40대'
            elif(age>=50 and age<60):
                age = '50대'
            else:
                age = '60대이상'
            up_agelist.append(age)         
            up_bdrnklist.append(mbdrnk)
            
        ziptup = list(zip(up_agelist,up_bdrnklist))
        ziplist = [list(row) for row in ziptup]
        
        teen_manlist = [i[1] for i in ziplist if i[0]=='10대']
        twe_manlist = [i[1] for i in ziplist if i[0]=='20대']
        thr_manlist = [i[1] for i in ziplist if i[0]=='30대']
        fou_manlist = [i[1] for i in ziplist if i[0]=='40대']
        fiv_manlist = [i[1] for i in ziplist if i[0]=='50대']
        ord_manlist = [i[1] for i in ziplist if i[0]=='60대이상']
        
        manteen_bdrnk = collections.Counter(teen_manlist)
        mantwe_bdrnk = collections.Counter(twe_manlist)
        manthr_bdrnk = collections.Counter(thr_manlist)
        manfou_bdrnk = collections.Counter(fou_manlist)
        manfiv_bdrnk = collections.Counter(fiv_manlist)
        manord_bdrnk = collections.Counter(ord_manlist)        
        
        manteen_bdrlist = []
        mantwe_bdrlist = []
        manthr_bdrlist = []
        manfou_bdrlist = []
        manfiv_bdrlist = []
        manord_bdrlist = []
        
        for i in range(len(bdrnk_n)):
            manteen_bdrlist.append(0)
            mantwe_bdrlist.append(0)
            manthr_bdrlist.append(0)
            manfou_bdrlist.append(0)
            manfiv_bdrlist.append(0)
            manord_bdrlist.append(0)
 
        for key,value in sorted(manteen_bdrnk.items()):
            for index,val in enumerate(manteen_bdrlist):
                manteen_bdrlist[key] = value

        for key,value in sorted(mantwe_bdrnk.items()):
            for index,val in enumerate(mantwe_bdrlist):
                mantwe_bdrlist[key] = value
    
        for key,value in sorted(manthr_bdrnk.items()):
            for index,val in enumerate(manthr_bdrlist):
                manthr_bdrlist[key] = value
    
        for key,value in sorted(manfou_bdrnk.items()):
            for index,val in enumerate(manfou_bdrlist):
                manfou_bdrlist[key] = value                                        
    
        for key,value in sorted(manfiv_bdrnk.items()):
            for index,val in enumerate(manfiv_bdrlist):
                manfiv_bdrlist[key] = value
                
        for key,value in sorted(manord_bdrnk.items()):
            for index,val in enumerate(manord_bdrlist):
                manord_bdrlist[key] = value         

        # 여성 구매기반 음료 취향        
        wombdrnk = MdOrdrM.objects.annotate(year = Substr("ordr__user__user_bir",1,4)).select_related("stor_m__menu").filter(ordr__user__gen=1).values_list("stor_m__menu__drnk_t","year")
        wombdrnk_list = list(wombdrnk)
         
        wup_agelist = []
        wup_bdrnklist = []
        
        for wmyear in wombdrnk_list:
            wmbdrnk = wmyear[0]
            wmyear = int(wmyear[1])
            wage = today - wmyear
            #print(age)
            if(wage >=10 and wage<20):
                wage = '10대'
            elif(wage>=20 and wage<30):
                wage = '20대'
            elif(wage>=30 and wage<40):
                wage = '30대'
            elif(wage>=40 and wage<50):
                age = '40대'
            elif(wage>=50 and wage<60):
                wage = '50대'
            else:
                wage = '60대이상'
            wup_agelist.append(wage)         
            wup_bdrnklist.append(wmbdrnk)
            
        wziptup = list(zip(wup_agelist,wup_bdrnklist))
        wziplist = [list(row) for row in wziptup]
        
        teen_womanlist = [i[1] for i in wziplist if i[0]=='10대']
        twe_womanlist = [i[1] for i in wziplist if i[0]=='20대']
        thr_womanlist = [i[1] for i in wziplist if i[0]=='30대']
        fou_womanlist = [i[1] for i in wziplist if i[0]=='40대']
        fiv_womanlist = [i[1] for i in wziplist if i[0]=='50대']
        ord_womanlist = [i[1] for i in wziplist if i[0]=='60대이상']
        
        womanteen_bdrnk = collections.Counter(teen_womanlist)
        womantwe_bdrnk = collections.Counter(twe_womanlist)
        womanthr_bdrnk = collections.Counter(thr_womanlist)
        womanfou_bdrnk = collections.Counter(fou_womanlist)
        womanfiv_bdrnk = collections.Counter(fiv_womanlist)
        womanord_bdrnk = collections.Counter(ord_womanlist)        
        
        womanteen_bdrlist = []
        womantwe_bdrlist = []
        womanthr_bdrlist = []
        womanfou_bdrlist = []
        womanfiv_bdrlist = []
        womanord_bdrlist = []
        
        for i in range(len(bdrnk_n)):
            womanteen_bdrlist.append(0)
            womantwe_bdrlist.append(0)
            womanthr_bdrlist.append(0)
            womanfou_bdrlist.append(0)
            womanfiv_bdrlist.append(0)
            womanord_bdrlist.append(0)
 
        for key,value in sorted(womanteen_bdrnk.items()):
            for index,val in enumerate(womanteen_bdrlist):
                womanteen_bdrlist[key] = value

        for key,value in sorted(womantwe_bdrnk.items()):
            for index,val in enumerate(womantwe_bdrlist):
                womantwe_bdrlist[key] = value
    
        for key,value in sorted(womanthr_bdrnk.items()):
            for index,val in enumerate(womanthr_bdrlist):
                womanthr_bdrlist[key] = value
    
        for key,value in sorted(womanfou_bdrnk.items()):
            for index,val in enumerate(womanfou_bdrlist):
                womanfou_bdrlist[key] = value                                        
    
        for key,value in sorted(womanfiv_bdrnk.items()):
            for index,val in enumerate(womanfiv_bdrlist):
                womanfiv_bdrlist[key] = value
                
        for key,value in sorted(womanord_bdrnk.items()):
            for index,val in enumerate(womanord_bdrlist):
                womanord_bdrlist[key] = value         

        context = {
            "bdrnk_n" : bdrnk_n,
            "bdrnk_list" : bdrnk_list,
            "manteen_bdrlist" : manteen_bdrlist,
            "mantwe_bdrlist" : mantwe_bdrlist,
            "manthr_bdrlist" : manthr_bdrlist,
            "manfou_bdrlist" : manfou_bdrlist,
            "manfiv_bdrlist" : manfiv_bdrlist,
            "manord_bdrlist" : manord_bdrlist,
            "womanteen_bdrlist" : womanteen_bdrlist,
            "womantwe_bdrlist" : womantwe_bdrlist,
            "womanthr_bdrlist" : womanthr_bdrlist,
            "womanfou_bdrlist" : womanfou_bdrlist,
            "womanfiv_bdrlist" : womanfiv_bdrlist,
            "womanord_bdrlist" : womanord_bdrlist,            
            }
        return HttpResponse(template.render(context,request))
    
#구매기반 디저트 취향    
class BdsrtView(View):
    def get(self,request):
        template = loader.get_template("md_admin/bdsrtstatis.html")
        today = datetime.today().year
        #구매한 음료 분류 정보
        bdsrt = MdOrdrM.objects.select_related("stor_m__menu").values("stor_m__menu__dsrt_t")
        bdsrt = list(m['stor_m__menu__dsrt_t'] for m in bdsrt)
        # 음료분류 아이디 -1은 삭제
        bdsrt = [item for item in bdsrt if item != -1]
        # print(bdsrt)  
        dict_bdsrt = {}
        dict_bdsrt = collections.Counter(bdsrt)
        
        bdsrt_n = MdDsrtT.objects.values("dsrt_t_name").order_by("dsrt_t_id")
        bdsrt_n = list(m['dsrt_t_name'] for m in bdsrt_n)
        bdsrt_n.remove('없음')       
        
        bdsrt_list  = []
        
        for i in range(len(bdsrt_n)):
            bdsrt_list.append(0)
        print(bdsrt_list)
        
        for key,value in sorted(dict_bdsrt.items()):
            for index,val in enumerate(bdsrt_list):
                bdsrt_list[key] = value
        
        # 남성 구매기반 디저트 취향        
        mbdsrt = MdOrdrM.objects.annotate(year = Substr("ordr__user__user_bir",1,4)).select_related("stor_m__menu").filter(ordr__user__gen=0).values_list("stor_m__menu__dsrt_t","year")
        mbdsrt_list = list(mbdsrt)
        # print(mbdsrt_list)
        
        up_agelist = []
        up_bdsrtlist = []
        
        for myear in mbdsrt_list:
            mbdsrt = myear[0]
            myear = int(myear[1])
            age = today - myear
            #print(age)
            if(age >=10 and age<20):
                age = '10대'
            elif(age>=20 and age<30):
                age = '20대'
            elif(age>=30 and age<40):
                age = '30대'
            elif(age>=40 and age<50):
                age = '40대'
            elif(age>=50 and age<60):
                age = '50대'
            else:
                age = '60대이상'
           
            up_agelist.append(age)         
            up_bdsrtlist.append(mbdsrt)
            up_bdsrtlist = [item for item in up_bdsrtlist if item != -1]
            print(up_bdsrtlist)

        ziptup = list(zip(up_agelist,up_bdsrtlist))
        ziplist = [list(row) for row in ziptup]  

        teen_manlist = [i[1] for i in ziplist if i[0]=='10대']
        twe_manlist = [i[1] for i in ziplist if i[0]=='20대']
        thr_manlist = [i[1] for i in ziplist if i[0]=='30대']
        fou_manlist = [i[1] for i in ziplist if i[0]=='40대']
        fiv_manlist = [i[1] for i in ziplist if i[0]=='50대']
        ord_manlist = [i[1] for i in ziplist if i[0]=='60대이상']

        manteen_bdsrt = collections.Counter(teen_manlist)
        print(manteen_bdsrt)
        mantwe_bdsrt = collections.Counter(twe_manlist)
        manthr_bdsrt = collections.Counter(thr_manlist)
        manfou_bdsrt = collections.Counter(fou_manlist)
        manfiv_bdsrt = collections.Counter(fiv_manlist)
        manord_bdsrt = collections.Counter(ord_manlist)
        
        manteen_bdslist = []
        mantwe_bdslist = []
        manthr_bdslist = []
        manfou_bdslist = []
        manfiv_bdslist = []
        manord_bdslist = []
        
        for i in range(len(bdsrt_n)):
            manteen_bdslist.append(0)
            mantwe_bdslist.append(0)
            manthr_bdslist.append(0)
            manfou_bdslist.append(0)
            manfiv_bdslist.append(0)
            manord_bdslist.append(0)
            
        for key,value in sorted(manteen_bdsrt.items()):
            for index,val in enumerate(manteen_bdslist):
                manteen_bdslist[key] = value

        for key,value in sorted(mantwe_bdsrt.items()):
            for index,val in enumerate(mantwe_bdslist):
                mantwe_bdslist[key] = value
    
        for key,value in sorted(manthr_bdsrt.items()):
            for index,val in enumerate(manthr_bdslist):
                manthr_bdslist[key] = value
    
        for key,value in sorted(manfou_bdsrt.items()):
            for index,val in enumerate(manfou_bdslist):
                manfou_bdslist[key] = value                                        
    
        for key,value in sorted(manfiv_bdsrt.items()):
            for index,val in enumerate(manfiv_bdslist):
                manfiv_bdslist[key] = value
                
        for key,value in sorted(manord_bdsrt.items()):
            for index,val in enumerate(manord_bdslist):
                manord_bdslist[key] = value                               
                      
        # 여성 구매기반 디저트 취향        
        wmbdsrt = MdOrdrM.objects.annotate(year = Substr("ordr__user__user_bir",1,4)).select_related("stor_m__menu").filter(ordr__user__gen=1).values_list("stor_m__menu__dsrt_t","year")
        wmbdsrt_list = list(wmbdsrt)
        # print(mbdsrt_list)
        
        wup_agelist = []
        wup_bdsrtlist = []
        
        for wmyear in wmbdsrt_list:
            wmbdsrt = wmyear[0]
            wmyear = int(wmyear[1])
            wage = today - wmyear
            #print(age)
            if(wage >=10 and wage<20):
                wage = '10대'
            elif(wage>=20 and wage<30):
                wage = '20대'
            elif(wage>=30 and wage<40):
                wage = '30대'
            elif(wage>=40 and wage<50):
                wage = '40대'
            elif(wage>=50 and wage<60):
                wage = '50대'
            else:
                wage = '60대이상'
           
            wup_agelist.append(wage)         
            wup_bdsrtlist.append(wmbdsrt)
            wup_bdsrtlist = [item for item in wup_bdsrtlist if item != -1]

        wziptup = list(zip(wup_agelist,wup_bdsrtlist))
        wziplist = [list(row) for row in wziptup]  

        teen_womanlist = [i[1] for i in wziplist if i[0]=='10대']
        twe_womanlist = [i[1] for i in wziplist if i[0]=='20대']
        thr_womanlist = [i[1] for i in wziplist if i[0]=='30대']
        fou_womanlist = [i[1] for i in wziplist if i[0]=='40대']
        fiv_womanlist = [i[1] for i in wziplist if i[0]=='50대']
        ord_womanlist = [i[1] for i in wziplist if i[0]=='60대이상']

        womanteen_bdsrt = collections.Counter(teen_womanlist)
        womantwe_bdsrt = collections.Counter(twe_womanlist)
        womanthr_bdsrt = collections.Counter(thr_womanlist)
        womanfou_bdsrt = collections.Counter(fou_womanlist)
        womanfiv_bdsrt = collections.Counter(fiv_womanlist)
        womanord_bdsrt = collections.Counter(ord_womanlist)
        
        womanteen_bdslist = []
        womantwe_bdslist = []
        womanthr_bdslist = []
        womanfou_bdslist = []
        womanfiv_bdslist = []
        womanord_bdslist = []
        
        for i in range(len(bdsrt_n)):
            womanteen_bdslist.append(0)
            womantwe_bdslist.append(0)
            womanthr_bdslist.append(0)
            womanfou_bdslist.append(0)
            womanfiv_bdslist.append(0)
            womanord_bdslist.append(0)
            
        for key,value in sorted(womanteen_bdsrt.items()):
            for index,val in enumerate(womanteen_bdslist):
                womanteen_bdslist[key] = value

        for key,value in sorted(womantwe_bdsrt.items()):
            for index,val in enumerate(womantwe_bdslist):
                womantwe_bdslist[key] = value
    
        for key,value in sorted(womanthr_bdsrt.items()):
            for index,val in enumerate(womanthr_bdslist):
                womanthr_bdslist[key] = value
    
        for key,value in sorted(womanfou_bdsrt.items()):
            for index,val in enumerate(womanfou_bdslist):
                womanfou_bdslist[key] = value                                        
    
        for key,value in sorted(womanfiv_bdsrt.items()):
            for index,val in enumerate(womanfiv_bdslist):
                womanfiv_bdslist[key] = value
                
        for key,value in sorted(womanord_bdsrt.items()):
            for index,val in enumerate(womanord_bdslist):
                womanord_bdslist[key] = value        
        
        context = {
            "bdsrt_list" : bdsrt_list,
            "bdsrt_n" : bdsrt_n,
            "manteen_bdslist" : manteen_bdslist,
            "mantwe_bdslist" : mantwe_bdslist,
            "manthr_bdslist" : manthr_bdslist,
            "manfou_bdslist" : manfou_bdslist,
            "manfiv_bdslist" : manfiv_bdslist,
            "manord_bdslist" : manord_bdslist,
            "womanteen_bdslist" : manteen_bdslist,
            "womantwe_bdslist" : womantwe_bdslist,
            "womanthr_bdslist" : womanthr_bdslist,
            "womanfou_bdslist" : womanfou_bdslist,
            "womanfiv_bdslist" : womanfiv_bdslist,
            "womanord_bdslist" : womanord_bdslist,
            }
        return HttpResponse(template.render(context,request))

#회원유입/이탈률 
class IaoView(View):
    def get(self,request):
        template = loader.get_template("md_admin/iaostatis.html")
        #회원가입일 가져오기
        welmaddi = MdUser.objects.values("user_reg_ts").order_by("user_reg_ts")
        welmaddi = list(m["user_reg_ts"] for m in welmaddi)
        #회원가입일 데이터 타입 str로 변경
        welmaddi = list(map(str,welmaddi))
       
        #회원가입일 연월로 자르기 
        wellist = []
        for i in range(len(welmaddi)):            
            wellist.append(welmaddi[i][0:7])
        #print(wellist)
        
        #해당연월 가입한 수
        dict_welmaddi = {}
        dict_welmaddi = collections.Counter(wellist)
        
        #print(dict_welmaddi)
        list_welmaddi = []
        for key,value in sorted(dict_welmaddi.items()):
            list_welmaddi.append(value)
        #print(list_welmaddi)
        
        #연월 값 뽑기
        welyear = MdUser.objects.values("user_reg_ts").order_by("user_reg_ts")
        welyear = list(m["user_reg_ts"] for m in welyear)
        welyear = list(map(str,welmaddi))
        
        welyearlist = []
        for i in range(len(welyear)):            
            welyearlist.append(welmaddi[i][0:7])
        
        #중복값 제거
        upwelyearlist = []
        for i in welyearlist:
            if i not in upwelyearlist:
                upwelyearlist.append(i)
        
        #print(upwelyearlist)
        context = {
            "list_welmaddi" : list_welmaddi,
            "upwelyearlist" : upwelyearlist
            }
        return HttpResponse(template.render(context,request))

# 키워드 통계
class KeywordView(View):
    def get(self,request):
        template = loader.get_template("md_admin/keystatis.html")
        keyword = MdSrch.objects.values("srch_word")
        keyword = list(m['srch_word'] for m in keyword)
        dict_keyword = {}
        dict_keyword = dict(collections.Counter(keyword))
        dict_keyword = dict(dict_keyword)
        # print(dict_keyword)
        
        textlist = []
        weightlist = []
        for key,value in dict_keyword.items():
            textlist.append(key)
            weightlist.append(value)
        #print(textlist)
        #print(weightlist)
        
        
        data_list = []
        #json 형태의 맞게 list append
        for text,weight in zip(textlist,weightlist):
            data_list.append({"x":text,"weight":weight})
        
        context = {
            "data_list" : data_list,
            }
        return HttpResponse(template.render(context,request))