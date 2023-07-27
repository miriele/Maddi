from django.shortcuts import render, redirect
from django.views import View
from django.http.response import HttpResponse, HttpResponseNotFound
from django.template import loader
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from md_store.models import MdStor, MdMenu, MdStorM, MdStorReg
from md_member.models import MdUser

from django.utils import timezone
##################################################
    # 이주림
    # 지금은 비록 하드 코드로 박았지만..
    # 나중에 stor_id, user_id, menu_id 넘겨 받는거로 수정할 것이다!!
##################################################

class AddJumjuView(View):
    @method_decorator( csrf_exempt )
    def dispatch(self, request, *args, **kwargs):
        return View.dispatch(self, request, *args, **kwargs) 
    def get(self, request):
        
        #회원정보
        user_id = "abc001"
        user = MdUser.objects.get(user_id=user_id)
        user_name = user.user_name
        user_bir = user.user_bir
        
        #매장정보
        stor_id = 6
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
        stor_id = 6
        reg = MdStorReg.objects.get(stor_id=stor_id)
        reg_num = request.POST["regnum"]
        reg.reg_num = reg_num
        reg.save()
        
        return redirect("md_store:addjumjusuc")
    
class ImageRegView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return View.dispatch(self, request, *args, **kwargs)
    def get(self, request):
        template = loader.get_template("md_store/imagereg.html")
        context = {}
        return HttpResponse( template.render( context, request ) )
    def post(self, request):
        user_id = "abc001"
        stor_id = 6
        imgreg = request.FILES["imgreg"]
        reg_sub_ts = timezone.now()

        # MdStorReg 모델에서 stor_id가 1인 데이터 조회
        try:
            reg = MdStorReg.objects.get(stor_id=stor_id)
        except MdStorReg.DoesNotExist:
            # 데이터가 없을 경우, 새로 생성하여 저장
            reg = MdStorReg(
                user_id=user_id,
                stor_id=stor_id,
                reg_sub_ts=reg_sub_ts,
            )

        reg.reg_img = imgreg
        reg.save()
        
        return redirect( "md_store:addjumju")

class AddMenuView(View):
    def get(self, request):
        template = loader.get_template("md_store/addmenu.html")
        stor_id = 1  
        stor = MdStor.objects.get(stor_id=stor_id)
        context = {
            'stor_name': stor.stor_name
            }
        return HttpResponse( template.render( context, request ) )
        
    def post(self, request):
        stor_id = 4
        menu_id = 1
        ice_t_id = request.POST["menucate"]
        menu_t_id = request.POST["menutype"]
        stor_m_pric = request.POST["menuprice"]
        stor_m_name = request.POST["menuname"]
        stor_m_cal = request.POST["menukcal"]
        stor_m_info = request.POST["menuinfo"]
        imgmenu = None
        
        new_stormenu = MdStorM.objects.create(
            stor_id = stor_id,
            menu_id = menu_id,
            ice_t_id = ice_t_id,
            menu_t_id = menu_t_id,
            stor_m_pric = stor_m_pric,
            stor_m_name = stor_m_name,
            stor_m_cal = stor_m_cal,
            stor_m_info = stor_m_info,
            stor_m_img = imgmenu,
            
            )
        return redirect( "md_store:addmenu")
    
class ImageMenuView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return View.dispatch(self, request, *args, **kwargs)
    def get(self, request):
        template = loader.get_template("md_store/imagemenu.html")
        context = {}
        return HttpResponse(template.render(context, request))
    def post(self, request):
        stor_m_id = 2883543
        storm = MdStorM.objects.get(stor_m_id=stor_m_id)
        imgmenu = request.FILES["imgmenu"]
        storm.stor_m_img = imgmenu
        storm.save()
        
        return redirect("md_store:addmenusuc")
    
class StoreView(View):
    @method_decorator( csrf_exempt )
    def dispatch(self, request, *args, **kwargs):
        return View.dispatch(self, request, *args, **kwargs) 
    def get(self, request):
        stor_id = 1
        try:
            store = MdStor.objects.get(stor_id=stor_id)
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
            
            stor_img = store.stor_img
            
            context = {
                'dto': store,
                'stor_type': stor_type,
                'stor_tel': stor_tel,
                'stor_id' : stor_id,
                'stor_t_id' : stor_t_id,
                'stor_img' : stor_img,
                'user_ids' : user_ids
            }
            
            return render(request, 'md_store/store.html', context)
        
        except MdStor.DoesNotExist:
            return HttpResponseNotFound()
        
    def post(self, request):
        stor_id = request.POST["stor_id"]
        stor_tel = request.POST.get("tel")
        
        try:
            store = MdStor.objects.get(stor_id=stor_id)
            store.stor_tel = stor_tel
            store.save()
            
            return redirect("md_store:store")
        
        except MdStor.DoesNotExist:
            return HttpResponseNotFound()

class ImageStoreView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return View.dispatch(self, request, *args, **kwargs)
    def get(self, request):
        template = loader.get_template("md_store/imagestore.html")
        context = {}
        return HttpResponse( template.render( context, request ) )
    def post(self, request):
        stor_id =1
        store = MdStor.objects.get(stor_id=stor_id)
        imgstor = request.FILES["imgstor"]
    
        store.stor_img = imgstor
        stor_t_id = store.stor_t_id
        bjd_code = store.bjd_code
        area_t = store.area_t
    
        store.save()
    
        return redirect("md_store:store")

class MenuInfoView(View):
    def get(self, request):
        stor_m_id = 2883543
        try:
            storem = MdStorM.objects.get(stor_m_id=stor_m_id)
            
            if storem.menu_t_id == 0:
                menu_type = "일반"
            else:
                menu_type = "시그니처"
            stor_m = MdStorM.objects.get(stor_m_id=stor_m_id)
            menu = stor_m.menu
            dsrt_t = menu.dsrt_t
            drnk_t = menu.drnk_t
                
            context = {
                'dto': storem,
                'stor_m_pric': storem.stor_m_pric,
                'stor_m_name': storem.stor_m_name,
                'stor_m_cal': storem.stor_m_cal,
                'stor_m_info': storem.stor_m_info,
                'stor_m_img': storem.stor_m_img,
                'menu_type': menu_type,
            }

            return render(request, 'md_store/menuinfo.html', context)

        except MdStorM.DoesNotExist:
            return HttpResponseNotFound()

class MenuListView(View):
    def get(self, request):
        stor_id = 1
        try:
            menu_list = MdStorM.objects.filter(stor__stor_id=stor_id)

            context = {
                'menu_list': menu_list,
            }

            return render(request, 'md_store/menulist.html', context)

        except MdStorM.DoesNotExist:
            return HttpResponseNotFound()
    def post(self, request):
        stor_id = request.POST["stor_id"]
        stor_m_id = request.POST["stor_m_id"]
        return HttpResponse(request)
    

      


class StoreUserView(View):
    @method_decorator( csrf_exempt )
    def dispatch(self, request, *args, **kwargs):
        return View.dispatch(self, request, *args, **kwargs) 
    def get(self, request):
        stor_id = request.GET.get("stor_id")
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
            
            stor_img = store.stor_img
            
            context = {
                'dto': store,
                'stor_type': stor_type,
                'stor_tel': stor_tel,
                'stor_id' : stor_id,
                'stor_t_id' : stor_t_id,
                'stor_img' : stor_img,
                'user_ids' : user_ids,
                'menu_list': menu_list,
            }
            
          
            return render(request, 'md_store/storeuser.html', context)
        
        except MdStor.DoesNotExist:
            return HttpResponseNotFound()
        
    def post(self, request):
        pass
            
class MypageJumjuView(View):
    def get(self, request):
        template = loader.get_template("md_store/mypagejumju.html")
        context = {}
        user_id = "abc001"
        user = MdUser.objects.get(user_id=user_id)
        user_name = user.user_name
        
        context = {
            "user_name":user_name,
            }
        
        return HttpResponse( template.render( context, request ) )
    
class AddJumjuSucView(View):
    def get(self, request):
        template = loader.get_template("md_store/addjumjusuc.html")
        context = {}
        
        return HttpResponse( template.render( context, request ) )

class AddMenuSucView(View):
    def get(self, request):
        template = loader.get_template("md_store/menuinfo.html")
        context = {}
        
        return HttpResponse( template.render( context, request ) )
    