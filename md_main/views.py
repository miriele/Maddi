from django.shortcuts import render, redirect
from django.views.generic.base import View
import logging
from django import template
from django.template import loader
from django.http.response import HttpResponse
from md_store.models import MdStorM, MdStor
from md_combi.models import MdCombM, MdComb
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

logger = logging.getLogger(__name__)

class MainView(View):
    def get(self,request):
        template = loader.get_template("md_main/main.html")
        memid = request.session.get("memid")
        gid = request.session.get("gid")
        
        # logger.debug(memid)
        # logger.debug(gid)
        tdtos = MdStorM.objects.select_related("menu").filter(menu__dsrt_t=-1).order_by('?')[:5]
        ddtos = MdStorM.objects.select_related("menu").filter(menu__drnk_t=-1).order_by('?')[:5]
        rdtos = MdComb.objects.all()
        print(rdtos)
        mdtos = MdCombM.objects.select_related("menu").all()
        if memid:
            context = {
                "memid":memid,
				"gid" :gid,
                "tdtos":tdtos,
                "ddtos":ddtos,
                "rdtos":rdtos,
                "mdtos":mdtos,      
                }
        else:
            context={
                "tdtos":tdtos,
                "ddtos":ddtos,
                "rdtos":rdtos,
                "mdtos":mdtos,
                }
        return HttpResponse(template.render(context,request))
    def post(self,request):
        pass
    
class SearchView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return View.dispatch(self, request, *args, **kwargs)    
    def get(self,request):
        template = loader.get_template("md_main/searchlist.html")
        count= MdStor.objects.all().count()
        if count ==0:
            context = {
                "count":count,
            }
        searchtext=request.GET.get("searchtext")
        sdtos = MdStor.objects.all()
        # ddtos = MdStorM.objects.all().select_related("stor").select_related("menu").filter(menu__drnk_t=-1)
        # tdtos = MdStorM.objects.all().select_related("menu").select_related("stor").filter(menu__dsrt_t=-1)
        if searchtext:
            sdtos = sdtos.filter(stor_name__icontains=searchtext)
            # ddtos = ddtos.filter(stor__stor_name__icontains=searchtext)
            # tdtos = tdtos.filter(stor__stor_name__icontains=searchtext)
            count = sdtos.all().count()
        context = {
            "sdtos":sdtos,
            "count":count,
            # "ddtos":ddtos,
            # "tdtos":tdtos,
            }
        return HttpResponse(template.render(context,request))

class MapView(View):
    def get(self,request):
        template = loader.get_template("md_main/map.html")
        # addr = request.GET("centerAddr")
        # print(addr) 
        context = {}
        return HttpResponse(template.render(context,request))