from django.shortcuts import render, redirect
from django.views.generic.base import View
import logging
from django import template
from django.template import loader
from django.http.response import HttpResponse
from md_store.models import MdMenu, MdStor

logger = logging.getLogger(__name__)

class MainView(View):
    def get(self,request):
        template = loader.get_template("md_main/main.html")
        stor_name = MdStor.objects.only("stor_name")
        tdtos = MdMenu.objects.filter(dsrt_t_id=-1)[:5]
        ddtos = MdMenu.objects.exclude(dsrt_t_id=-1)[:5]
        memid = request.session.get("memid")
        if memid:
            context = {
                "memid":memid
                }
        else:
            context={
                "tdtos":tdtos,
                "ddtos":ddtos,
                "stor_name":stor_name,
                }
        return HttpResponse(template.render(context,request))
    def post(self,request):
        pass
