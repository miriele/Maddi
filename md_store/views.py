from django.shortcuts import render
from django.views.generic.base import View
from django.template import loader
from django.http.response import HttpResponse, HttpResponseNotFound
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from md_store.models import MdStor

from django.conf import settings

class InfoView(View):
    def get(self, request):
        stor_id = 26234
        store = MdStor.objects.get(stor_id=stor_id)
        
        image_filename = store.stor_img 
        
        context = {
            'dto': store,
            'image_filename': image_filename 
        }
        return render(request, 'md_store/info.html', context)

class MenuListView(View):
    def get(self, request):
        template = loader.get_template("md_store/menulist.html")
        return HttpResponse(template.render())



    