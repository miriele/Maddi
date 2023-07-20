from django.shortcuts import render, redirect
from django.views import View
from django.http.response import HttpResponse, HttpResponseNotFound
from django.template import loader
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from md_store.models import MdStor, MdMenu, MdMenuT, MdStorM
from md_member.models import MdUser
##################################################
    # 이주림
    # 지금은 비록 하드 코드로 박았지만..
    # 나중에 stor_id, user_id, menu_id 넘겨 받는거로 수정할 것이다!!
##################################################

class StoreView(View):
    @method_decorator( csrf_exempt )
    def dispatch(self, request, *args, **kwargs):
        return View.dispatch(self, request, *args, **kwargs) 
    
    def get(self, request):
        stor_id = 6
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

class ImageView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return View.dispatch(self, request, *args, **kwargs)
    def get(self, request):
        template = loader.get_template("md_store/image.html")
        context = {}
        return HttpResponse( template.render( context, request ) )
    def post(self, request):
        stor_id = 6
        store = MdStor.objects.get(stor_id=stor_id)
        img = request.FILES["img"]
    
        store.stor_img = img
        stor_t_id = store.stor_t_id
        bjd_code = store.bjd_code
        area_t = store.area_t
    
        store.save()
    
        return redirect("md_store:store")

class MenuInfoView(View):
    def get(self, request):
        stor_m_id = 141
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
        stor_m_id = 141
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
            
            if dsrt_t:
                if dsrt_t.dsrt_t_id == 0:
                    dsrt_t_name = dsrt_t.dsrt_t_name
                else:
                    dsrt_t_name = "없음"
            else:
                dsrt_t_name = "없음"
            
            if drnk_t:
                drnk_t_name = drnk_t.drnk_t_name
            else:
                drnk_t_name = "없음"
                
            context = {
                'dto': storem,
                'stor_m_pric': storem.stor_m_pric,
                'stor_m_name': storem.stor_m_name,
                'stor_m_cal': storem.stor_m_cal,
                'stor_m_info': storem.stor_m_info,
                'stor_m_img': storem.stor_m_img,
                'menu_type': menu_type,
            }

            return render(request, 'md_store/menulist.html', context)

        except MdStorM.DoesNotExist:
            return HttpResponseNotFound()
    def post(self,request):
        stor_id = request.POST["stor_id"]
        return HttpResponse( request  )
    
class AddMenuView(View):
    def get(self,request):
        context = {}
        return render(request, 'md_store/addmenu.html', context)

class AddJumjuView(View):
    @method_decorator( csrf_exempt )
    def dispatch(self, request, *args, **kwargs):
        return View.dispatch(self, request, *args, **kwargs) 
    def get(self,request):
        user_id = "abc002"
        user = MdUser.objects.get(user_id=user_id)
        user_name = user.user_name
        user_bir = user.user_bir
        
        stor_id = 6
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
            "user_id":user_id,
            "user_ids":user_ids,
            "user_name":user_name,
            "user_bir":user_bir,
            'dto': store,
            'stor_type': stor_type,
            'stor_tel': stor_tel,
            'stor_id' : stor_id,
            'stor_t_id' : stor_t_id,
            'stor_img' : stor_img,
            }
        return render(request, 'md_store/addjumju.html', context)
    
    def post(self,request):
        stor_id = request.POST["stor_id"]
        user_id = request.POST["user_id"]
        
        user = MdUser.objects.get(user_id=user_id)
        store = MdStor.objects.get(stor_id=stor_id)
        
        store.user_id = user_id
        user.user_g_id = 6
        user.save()
        store.save()
        
        return redirect("md_store:store")
    
class StoreUserView(View):
    @method_decorator( csrf_exempt )
    def dispatch(self, request, *args, **kwargs):
        return View.dispatch(self, request, *args, **kwargs) 
    def get(self, request):
        stor_id = 6
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
            
            return render(request, 'md_store/storeuser.html', context)
        
        except MdStor.DoesNotExist:
            return HttpResponseNotFound()
        
    def post(self, request):
        pass
            
class MypageJumjuView(View):
    def get(self, request):
        template = loader.get_template("md_store/mypagejumju.html")
        context = {}
        user_id = "abc002"
        user = MdUser.objects.get(user_id=user_id)
        user_name = user.user_name
        
        context = {
            "user_name":user_name,
            }
        
        return HttpResponse( template.render( context, request ) ) 
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            