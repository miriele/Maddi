from django.shortcuts import render
from django.views.generic.base import View
from django.template import loader
from django.http.response import HttpResponse, HttpResponseNotFound
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from md_store.models import MdStor

from django.conf import settings
##################################################
# 이주림
# 지금은 비로 하드 코드로 박았지만..
# 나중에 stor_id 넘겨 받는거로 수정할 것이다!!
##################################################
class StoreView(View):
    def get(self, request):
        stor_id = 26234
        store = MdStor.objects.get(stor_id=stor_id)
        
        if store.stor_t == 0:
            stor_type = "개인"
        else:
            stor_type = "프랜차이즈"

        context = {
            'dto': store,
            'stor_type': stor_type
        }
        return render(request, 'md_store/store.html', context)


class MenuView(View):
    def get(self, request):
        template = loader.get_template("md_store/menu.html")
        return HttpResponse(template.render())



    