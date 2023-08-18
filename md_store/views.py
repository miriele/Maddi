from django.shortcuts import render, redirect, reverse
from django.views import View
from django.http.response import HttpResponse, HttpResponseNotFound
from django.template import loader
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from md_store.models import MdStor, MdMenu, MdStorM, MdStorReg, MdMAlgy, MdAlgyT
from md_member.models import MdUser
from django.utils import timezone
from md_favorite.models import MdFavorite
from asgiref.server import logger
from datetime import datetime
import logging

# 로그
logger = logging.getLogger( __name__ )

class TestStoreView(View):
    def get(self, request):
        try:
            store_list = MdStor.objects.filter(stor_id__gte=12012, stor_id__lte=1)

            context = {
                'store_list': store_list,
            }

            return render(request, 'md_store/teststore.html', context)

        except MdStor.DoesNotExist:
            return HttpResponseNotFound()

    def post(self, request):
        pass

class AddJumjuView(View):
    @method_decorator( csrf_exempt )
    def dispatch(self, request, *args, **kwargs):
        return View.dispatch(self, request, *args, **kwargs) 

    def get(self, request):
        
        #회원정보
        user_id = request.session.get('memid')
        user = MdUser.objects.get(user_id=user_id)
        user_name = user.user_name
        user_bir = user.user_bir
        
        #매장정보
        stor_id = request.GET['stor_id']
        store = MdStor.objects.get(stor_id=stor_id)
        stor_t_id = store.stor_t_id
        
        if store.stor_t_id == 0:
            stor_type = "개인"
        else:
            stor_type = "프랜차이즈"
    
        stor_tel = store.stor_tel if store.stor_tel else "등록된 연락처가 없습니다"
        user_ids = store.user_id if store.user_id else "등록된 점주가 없습니다"
        stor_img = store.stor_img
        
        try:
            reg = MdStorReg.objects.get(stor_id=stor_id)
            reg_img = reg.reg_img
            reg_num = reg.reg_num
        except MdStorReg.DoesNotExist:
            reg_img = None
            reg_num = None
        
        context = {
                "user_id": user_id,
                "user_ids": user_ids,
                "user_name": user_name,
                "user_bir": user_bir,
                'dto': store,
                'stor_type': stor_type,
                'stor_tel': stor_tel,
                'stor_id': stor_id,
                'stor_t_id': stor_t_id,
                'stor_img': stor_img,
                'reg_img' : reg_img,
                'reg_num' : reg_num,
            }
        return render(request, 'md_store/addjumju.html', context)
    
    def post(self, request):
        user_id     = request.POST['user_id']
        stor_id     = request.POST['stor_id']
        reg_num     = request.POST["regnum"]
        imgreg      = request.FILES["imgreg"]
        reg_sub_ts  = timezone.now()
        
        logger.debug(f'imgreg : {imgreg}')
        
        exist_stor_reg = MdStorReg.objects.filter(user_id=user_id).first()

        if exist_stor_reg:
            context = {
            }
            return render(request, 'md_store/addjumjufail.html', context)

        MdStorReg.objects.create(
            user_id = user_id,
            stor_id = stor_id,
            reg_num = reg_num,
            reg_img  = imgreg,
            reg_sub_ts = reg_sub_ts,
        )
        
        return redirect("md_store:addjumjusuc")

# class AddMenuView(View):
#     def get(self, request):
#         template = loader.get_template("md_store/addmenu.html")
#         stor_id = request.GET["stor_id"] 
#         stor = MdStor.objects.get(stor_id=stor_id)
#         context = {
#             'stor_name': stor.stor_name,
#             'stor_id' : stor_id
#             }
#         return HttpResponse( template.render( context, request ) )
#
#     def post(self, request):
#         stor_id = request.POST["stor_id"]
#         ice_t_id = request.POST["ice"]
#         menu_t_id = request.POST["menutype"]
#         stor_m_pric = request.POST["menupric"]
#         stor_m_name = request.POST["menuname"]
#         stor_m_cal = request.POST["menukcal"]
#         stor_m_info = request.POST["menuinfo"]
#         algy_t_list = request.POST.getlist("algy[]") 
#         imgmenu = request.FILES["imgmenu"]
#
#         MdStorM.objects.create(
#             stor_id=stor_id,
#             menu_id=menu_id,  # 새로운 MdMenu 객체의 menu_id 값을 사용
#             menu_t_id=menu_t_id,
#             stor_m_pric=stor_m_pric,
#             stor_m_name=stor_m_name,
#             stor_m_cal=stor_m_cal,
#             stor_m_info=stor_m_info,
#             stor_m_img=imgmenu,
#             ice_t_id=ice_t_id,
#         )
#
#         for algy_t_id in algy_t_list:
#             if not MdMAlgy.objects.filter(menu_id=menu_id, algy_t_id=algy_t_id).exists():
#                 MdMAlgy.objects.create(menu_id=menu_id, algy_t_id=algy_t_id)
#
#         return render(request, 'md_store/addmenusuc.html')
    
class StoreView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    def get(self, request):
        
        stor_id = request.GET['stor_id']
        memid = request.session.get("memid")
        gid = request.session.get("gid")
        
        stor = MdStor.objects.get(stor_id=stor_id)
        
        if stor.stor_t_id == 0:
            stor_type = "개인"
        else:
            stor_type = "프랜차이즈"
        
        template = loader.get_template( "md_store/store.html")
        context={
            "stor_id"   :stor_id,
            "memid"     :memid,
            "gid"       :gid,
            "stor"      :stor,
            "stor_type" :stor_type,
            }
        return HttpResponse( template.render( context, request ) )

    def post(self, request):
        
        memid = request.session.get("memid")
        gid = request.session.get("gid")
        stor_id     = request.POST["stor_id"]
        stor_img    = request.POST["stor_img"]
        
        Nstor_img = request.FILES.get("Nstor_img")  
        
        # 이미지 업로드 안 했을 시 기본으로 저장
        if Nstor_img  == None :
            Nstor_img = stor_img
        else :
            Nstor_img 
        logger.debug(f'Nstor_img : {Nstor_img}')  
        
        stor = MdStor.objects.get(stor_id=stor_id)
        
        stor = MdStor(
            stor_id     = stor_id,
            stor_t_id   = stor.stor_t_id,
            user_id     = memid,
            bjd_code    = stor.bjd_code,
            area_t_id   = stor.area_t_id,
            stor_img    = Nstor_img,
            stor_name   = stor.stor_name,
            stor_addr   = stor.stor_addr,
            stor_lati   = stor.stor_lati,
            stor_long   = stor.stor_long,
            stor_tel    = request.POST["stor_tel"],
            stor_num    = stor.stor_num,  
            )
        stor.save()
        template = loader.get_template( "md_store/mypagejumju.html")
        context={
            "stor_id"   :stor_id,
            "memid"     :memid,
            "gid"       :gid,
            }
        return HttpResponse( template.render( context, request ) )
        # return redirect("/md_store/store?stor_id=request.POST['stor_id']")
        

class MenuListView(View):
    def get(self, request):
        memid     = request.session.get("memid")
        gid       = request.session.get("gid")
        stor_id   =  request.GET.get("stor_id")
        store     = MdStor.objects.get(stor_id=stor_id)
        menu_list = MdStorM.objects.filter(stor__stor_id=stor_id)
        stor_t_id = store.stor_t_id
        
        if store.stor_t_id == 0:
            stor_type = "개인"
        else:
            stor_type = "프랜차이즈"
        
        if store.stor_tel:
            stor_tel = store.stor_tel
        else:
            stor_tel = "등록된 연락처가 없습니다"
        
        if store.user_id:
            user_ids= store.user_id
        else:
            user_ids = "등록된 점주가 없습니다"
        
        stor_img_str = str(store.stor_img)
        stor_img = stor_img_str.replace(' /images', '')
        
        context = {
            'dto': store,
            'stor_type': stor_type,
            'stor_tel': stor_tel,
            'stor_id' : stor_id,
            'stor_t_id' : stor_t_id,
            'stor_img' : stor_img,
            'user_ids' : user_ids,
            'menu_list': menu_list,
            'memid' : memid,
            'gid' : gid,
        }

        return render(request, 'md_store/menulist.html', context)

    def post(self,request):
        pass


class MenuInfoView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    def get(self, request):
        memid = request.session.get("memid")
        gid = request.session.get("gid")        
        stor_m_id = request.GET['stor_m_id']
        storem = MdStorM.objects.get(stor_m_id=stor_m_id)
        menu_id = storem.menu_id
        stor_id = storem.stor_id
        menu = MdMenu.objects.get(menu_id=menu_id)
        
        m_algy = MdMAlgy.objects.filter(menu_id = menu_id)
        
        md_algy_t = MdAlgyT.objects.order_by("algy_t_id")
        
        dsrt_t = menu.dsrt_t_id
        drnk_t = menu.drnk_t_id
        
        cate = ""
        
        if dsrt_t == -1:
            cate = -1   #음료
        elif drnk_t == -1:
            cate = 0    #디저트
        else:
            cate = 1    #선택
        
        context = {
            'dto': storem,
            'ice' : storem.ice_t_id,
            'stor_m_id': stor_m_id,
            'menu_id' : menu_id,
            'stor_m_name': storem.stor_m_name,
            'stor_m_pric': storem.stor_m_pric,
            'dsrt_t' : dsrt_t,
            'drnk_t' : drnk_t,
            'stor_m_cal': storem.stor_m_cal,
            'stor_m_info': storem.stor_m_info,
            'stor_m_img': storem.stor_m_img,
            'cate' : cate,
            'stor_id' : stor_id,
            'm_algy' : m_algy,
            'md_algy_t' : md_algy_t,
            'memid' : memid,
            'gid' : gid,            
        }

        return render(request, 'md_store/menuinfo.html', context)
    
    def post(self, request):
        stor_m_id = request.POST['stor_m_id']
        menu_id = request.POST['menu_id']
        
        storem = MdStorM.objects.get(stor_m_id=stor_m_id)
        algy = MdMAlgy.objects.filter(menu_id=menu_id)
        menu = MdMenu.objects.filter(menu_id=menu_id)
        
        stor_m_pric = request.POST["menupric"]
        stor_m_cal = request.POST["menukcal"]
        stor_m_info = request.POST["menuinfo"]
        menu_t_id = request.POST["menutype"]
        
        # algy_t_list = request.POST.getlist("algy[]")
        list_algy = request.POST.getlist("md_algy_t")
        # 디비서 가져온거
        m_algy = MdMAlgy.objects.filter(menu_id =menu_id)
        logger.debug(f'm_algy : {m_algy}')
        
        for ma in m_algy :
            ma.delete()
        
        for a in list_algy :
            if a :
                dtoa = MdMAlgy(
                    menu_id     = menu_id,
                    algy_t_id   = a
                    )
                dtoa.save()
        
        imgmenuinfo = storem.stor_m_img = MdStorM.objects.get(stor_m_id=stor_m_id).stor_m_img

        if "imgmenuinfo" in request.FILES:
            imgmenuinfo = request.FILES["imgmenuinfo"]
            storem.stor_m_img = imgmenuinfo
        else:
            storem.stor_m_img = MdStorM.objects.get(stor_m_id=stor_m_id).stor_m_img
        
        # 알러지 정보를 업데이트
        # existing_algy_t_ids = MdMAlgy.objects.filter(menu_id=menu_id).values_list("algy_t_id", flat=True)
        # new_algy_t_ids = [int(algy_t_id) for algy_t_id in algy_t_list]
    
        # 기존 알러지를 삭제하고 새로운 알러지 정보를 추가
        # algy.exclude(algy_t_id__in=new_algy_t_ids).delete()
        # for algy_t_id in new_algy_t_ids:
        #     if algy_t_id not in existing_algy_t_ids:
        #         MdMAlgy.objects.create(menu_id=menu_id, algy_t_id=algy_t_id)
        
        stor_m_id = stor_m_id
        storem.stor_m_pric = stor_m_pric
        storem.stor_m_cal = stor_m_cal
        storem.stor_m_info = stor_m_info
        storem.stor_m_img = imgmenuinfo
        storem.menu_t_id = menu_t_id
        storem.save()
    
        return redirect(reverse("md_store:menuinfo") + f'?stor_m_id={stor_m_id}')
    
class StoreUserView(View):
    @method_decorator( csrf_exempt )
    def dispatch(self, request, *args, **kwargs):
        return View.dispatch(self, request, *args, **kwargs) 
    def get(self, request):
        stor_id = request.GET.get("stor_id")
        memid    = request.session.get("memid")
        gid      = request.session.get("gid")
        
        result = 0
        md_fav = MdFavorite.objects.filter(stor = stor_id, user_id =memid)
        
        for fav in md_fav :
            logger.debug(f'fav.user_id : {fav.user_id}')
            if fav.user_id == memid :
                result = 1
                break
        try:
            store = MdStor.objects.get(stor_id=stor_id)
            menu_list = MdStorM.objects.filter(stor__stor_id=stor_id)
            stor_t_id = store.stor_t_id
            
            if store.stor_t_id == 0:
                stor_type = "개인"
            else:
                stor_type = "프랜차이즈"
            
            if store.stor_tel:
                stor_tel = store.stor_tel
            else:
                stor_tel = "등록된 연락처가 없습니다"
            
            if store.user_id:
                user_ids= store.user_id
            else:
                user_ids = "등록된 점주가 없습니다"
            
            stor_img_str = str(store.stor_img)
            stor_img = stor_img_str.replace(' /images', '')
            
            
            context = {
                "result" : result,
                'dto': store,
                'stor_type': stor_type,
                'stor_tel': stor_tel,
                'stor_id' : stor_id,
                'stor_t_id' : stor_t_id,
                'stor_img' : stor_img,
                'user_ids' : user_ids,
                'menu_list': menu_list,
                'memid' : memid,
                'gid' : gid,
            }
            
          
            return render(request, 'md_store/storeuser.html', context)
        
        except MdStor.DoesNotExist:
            return HttpResponseNotFound()
        
    def post(self, request):
        pass
            
class MypageJumjuView(View):
    def get(self, request):
        template = loader.get_template("md_store/mypagejumju.html")
        memid =request.session.get("memid")
        gid = request.session.get("gid")
        user = MdUser.objects.get(user_id=memid)
        stor = MdStor.objects.get(user_id=memid)
        stor_id = stor.stor_id
        user_name = user.user_name
        
        context = {
            "user_name": user_name,
            "stor_id" : stor_id,
            "memid" : memid,
            "gid" : gid,
            }
        
        return HttpResponse( template.render( context, request ) )
    
class AddJumjuSucView(View):
    def get(self, request):
        template = loader.get_template("md_store/addjumjusuc.html")
        memid = request.session.get("memid")
        gid   = request.session.get("gid")
        context = {
            "memid" : memid,
            "gid"   : gid,
            }
        
        return HttpResponse( template.render( context, request ) )

class AddMenuSucView(View):
    def get(self, request):
        template = loader.get_template("md_store/menuinfo.html")
        context = {}
        
        return HttpResponse( template.render( context, request ) )
    

# 즐겨찾기용 옮김
class AddFavView( View ):
    @method_decorator( csrf_exempt )
    def dispatch(self, request, *args, **kwargs):
        return View.dispatch(self, request, *args, **kwargs)
    def post(self, request ):
        memid = request.session.get("memid")
        gid   = request.session.get("gid")
        
        stor_id = request.POST.get("stor_id","")    #7
        
        logger.debug(f'stor_id : {stor_id}')
        
        favo = MdFavorite.objects.filter( user = memid, stor = stor_id ).count()
        logger.debug(f'favo : {favo}')
        
        result = 0
        
        if favo == 0 :
            favo = MdFavorite(
                user_id    = memid,
                stor_id    = stor_id,
                fav_reg_ts = datetime.now()
                )
            favo.save()
            result = 1
        else :
            favo = MdFavorite.objects.filter( user = memid, stor = stor_id )
            favo.delete()
            result = 0
            
        logger.debug(f'result : {result}')

        return HttpResponse(result)

    