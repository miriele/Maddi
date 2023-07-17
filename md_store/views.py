from django.shortcuts import render
from django.views import View
from md_store.models import MdStor
from django.http.response import HttpResponse, HttpResponseNotFound
from django.template import loader


class StoreView(View):
    def get(self, request):
        stor_id = 19078
        try:
            store = MdStor.objects.get(stor_id=stor_id)
            
            if store.stor_t == 0:
                stor_type = "개인"
            else:
                stor_type = "프랜차이즈"
            
            if store.stor_tel:
                stor_tel = store.stor_tel
            else:
                stor_tel = "등록된 연락처가 없습니다"
            
            context = {
                'dto': store,
                'stor_type': stor_type,
                'stor_tel': stor_tel
            }
            return render(request, 'md_store/store.html', context)
        except MdStor.DoesNotExist:
            return HttpResponseNotFound()


class MenuView(View):
    def get(self, request):
        template = loader.get_template("md_store/menu.html")
        return HttpResponse(template.render())



    