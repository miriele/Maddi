from django.shortcuts import render
from django.views.generic.base import View
from django.template import loader
from django.http.response import HttpResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

class InfoView(View):
    def get(self, request):
        template = loader.get_template("md_store/info.html")
        return HttpResponse(template.render()) 
