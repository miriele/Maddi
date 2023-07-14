from django.shortcuts import render
from django.views.generic.base import View
from django.template import loader
from django.http.response import HttpResponse, HttpResponseNotFound
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from md_store.models import MdStor

class InfoView(View):
    def get(self, request):
        stor_id = 244  # Set the desired stor_id here
        store = MdStor.objects.get(stor_id=stor_id)
        context = {
            'dto': store
        }
        return render(request, 'md_store/info.html', context)
