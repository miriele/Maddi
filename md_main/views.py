from django.shortcuts import render, redirect
from django.views.generic.base import View
import logging
from django import template
from django.template import loader
from django.http.response import HttpResponse
from md_store.models import MdStorM
from md_combi.models import MdCombM

logger = logging.getLogger(__name__)

class MainView(View):
    def get(self,request):
        template = loader.get_template("md_main/main.html")
        memid = request.session.get("memid")
        tdtos = MdStorM.objects.select_related("menu").filter(menu__dsrt_t=-1)[:5]
        ddtos = MdStorM.objects.select_related("menu").filter(menu__drnk_t=-1)[:5]
        rdtos = MdCombM.objects.select_related("comb")[:5]
        if memid:
            context = {
                "memid":memid,
                "tdtos":tdtos,
                "ddtos":ddtos,
                "rdtos":rdtos,
                
                }
        else:
            context={
                "tdtos":tdtos,
                "ddtos":ddtos,
                "rdtos":rdtos,
                }
        return HttpResponse(template.render(context,request))
    def post(self,request):
        pass
