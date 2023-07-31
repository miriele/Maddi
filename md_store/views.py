from django.shortcuts import render, redirect
from django.views import View
from django.http.response import HttpResponse, HttpResponseNotFound
from django.template import loader
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from md_store.models import MdStor, MdMenu, MdStorM, MdStorReg, MdMAlgy
from md_member.models import MdUser
from django.utils import timezone


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
        user_id = "abc001"
        stor_id = 6
        reg_num = request.POST["regnum"]
        imgreg = request.FILES["imgreg"]
        reg_sub_ts = timezone.now()
        
        MdStorReg.objects.create(
            user_id = user_id,
            stor_id = stor_id,
            reg_num = reg_num,
            reg_img  = imgreg,
            reg_sub_ts = reg_sub_ts,
        )
        
        return redirect("md_store:addjumjusuc")

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
        ice_t_id = request.POST["ice"]
        menu_t_id = request.POST["menutype"]
        stor_m_pric = request.POST["menupric"]
        stor_m_name = request.POST["menuname"]
        stor_m_cal = request.POST["menukcal"]
        stor_m_info = request.POST["menuinfo"]
        algy_t_list = request.POST.getlist("algy[]") 
        imgmenu = request.FILES["imgmenu"]
        
        MdStorM.objects.create(
            stor_id = stor_id,
            menu_id = menu_id,
            menu_t_id = menu_t_id,
            stor_m_pric = stor_m_pric,
            stor_m_name = stor_m_name,
            stor_m_cal = stor_m_cal,
            stor_m_info = stor_m_info,
            stor_m_img = imgmenu,
            ice_t_id = ice_t_id,
            )
        
        for algy_t_id in algy_t_list:
            if not MdMAlgy.objects.filter(menu_id=menu_id, algy_t_id=algy_t_id).exists():
                MdMAlgy.objects.create(menu_id=menu_id, algy_t_id=algy_t_id)
            
        return redirect( "md_store:addmenu")
    
class StoreView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    def get(self, request):
        stor_id = 3 
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
                user_ids = store.user_id
            else:
                user_ids = "등록된 점주가 없습니다"

            stor_img = str(store.stor_img).replace('images/', '')

            
            context = {
                'dto': store,
                'stor_type': stor_type,
                'stor_tel': stor_tel,
                'stor_id': stor_id,
                'stor_t_id': stor_t_id,
                'stor_img': stor_img,
                'user_ids': user_ids
            }

            return render(request, 'md_store/store.html', context)

        except MdStor.DoesNotExist:
            return HttpResponseNotFound()

    def post(self, request):
        stor_id = 3
        stor_tel = request.POST["tel"]

        try:
            store = MdStor.objects.get(stor_id=stor_id)
            store.stor_tel = stor_tel

            imgstor = request.FILES["imgstor"]
            if imgstor:
                store.stor_img = imgstor

            store.save()

            return redirect("md_store:store")

        except MdStor.DoesNotExist:
            return HttpResponseNotFound()


class MenuInfoView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    def get(self, request):
        stor_m_id = 2883541
        menu_id = 1
        try:
            storem = MdStorM.objects.get(stor_m_id=stor_m_id)
            
            if storem.menu_t_id == 0:
                menu_type = "일반"
            else:
                menu_type = "시그니처"
                
            menu = MdMenu.objects.get(menu_id=menu_id)
            dsrt_t = menu.dsrt_t_id
            drnk_t = menu.drnk_t_id
            
            cate = ""
            
            if dsrt_t == -1:
                cate = -1
            elif drnk_t == -1:
                cate = 0
            else:
                cate = 1 
            
            context = {
                'dto': storem,
                'ice' : storem.ice_t_id,
                'stor_m_id': storem.stor_m_id,
                'stor_m_name': storem.stor_m_name,
                'stor_m_pric': storem.stor_m_pric,
                'dsrt_t' : dsrt_t,
                'drnk_t' : drnk_t,
                'stor_m_cal': storem.stor_m_cal,
                'stor_m_id': storem.stor_m_id,
                'stor_m_info': storem.stor_m_info,
                'stor_m_img': storem.stor_m_img,
                'menu_type': menu_type,
                'cate' : cate
            }

            return render(request, 'md_store/menuinfo.html', context)

        except MdStorM.DoesNotExist:
            return HttpResponseNotFound()
    
    def post(self, request):
        stor_m_id = 2883541
        menu_id = 1
        storem = MdStorM.objects.get(stor_m_id=stor_m_id)
    
        ice_t_id = request.POST["ice"]
        menu_t_id = request.POST["menutype"]
        stor_m_pric = request.POST["menupric"]
        stor_m_name = request.POST["menuname"]
        stor_m_cal = request.POST["menukcal"]
        stor_m_info = request.POST["menuinfo"]
        algy_t_list = request.POST.getlist("algy[]")
        imgmenuinfo = request.FILES["imgmenuinfo"]
    
        stor_m_id = stor_m_id
        storem.ice_t_id = ice_t_id
        storem.menu_t_id = menu_t_id
        storem.stor_m_pric = stor_m_pric
        storem.stor_m_name = stor_m_name
        storem.stor_m_cal = stor_m_cal
        storem.stor_m_info = stor_m_info
        storem.stor_m_img = imgmenuinfo
        storem.save()
    
        # 알러지 정보를 업데이트
        existing_algy_t_ids = MdMAlgy.objects.filter(menu_id=menu_id).values_list("algy_t_id", flat=True)
        new_algy_t_ids = [int(algy_t_id) for algy_t_id in algy_t_list]
    
        # 기존 알러지를 삭제하고 새로운 알러지 정보를 추가
        MdMAlgy.objects.filter(menu_id=menu_id).exclude(algy_t_id__in=new_algy_t_ids).delete()
        for algy_t_id in new_algy_t_ids:
            if algy_t_id not in existing_algy_t_ids:
                MdMAlgy.objects.create(menu_id=menu_id, algy_t_id=algy_t_id)
    
        return redirect("md_store:menulist")

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
            }
            
          
            return render(request, 'md_store/storeuser.html', context)
        
        except MdStor.DoesNotExist:
            return HttpResponseNotFound()
        
    def post(self, request):
        pass
            
class MypageJumjuView(View):
    def get(self, request):
        template = loader.get_template("md_store/mypagejumju.html")
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
    