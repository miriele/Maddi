from django.shortcuts import render, redirect
from django.views import View
from django.http.response import HttpResponse, HttpResponseNotFound
from django.template import loader
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from md_store.models import MdStor, MdMenu, MdMenuT

class StoreView(View):
    @method_decorator( csrf_exempt )
    def dispatch(self, request, *args, **kwargs):
        return View.dispatch(self, request, *args, **kwargs) 
    ##################################################
    # 이주림
    # 지금은 비로 하드 코드로 박았지만..
    # 나중에 stor_id 넘겨 받는거로 수정할 것이다!!
    ##################################################
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
            
            stor_img = store.stor_img
            
            context = {
                'dto': store,
                'stor_type': stor_type,
                'stor_tel': stor_tel,
                'stor_id' : stor_id,
                'stor_t_id' : stor_t_id,
                'stor_img' : stor_img,
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
            stor_img = store.stor_img
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
        stor_id = 1
        store = MdStor.objects.get(stor_id=stor_id)
        img = request.FILES["img"]
    
        store.stor_img = img
        stor_t_id = store.stor_t_id
        bjd_code = store.bjd_code
        area_t = store.area_t
    
        store.save()
    
        return redirect("md_store:store")
