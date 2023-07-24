from django.shortcuts import render, redirect
from django.views.generic.base import View
import logging
from django import template
from django.template import loader
from django.http.response import HttpResponse
from md_store.models import MdStorM, MdStor, MdMenu
from md_combi.models import MdCombM, MdComb
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.db.models.aggregates import Count, Sum
from md_order.models import MdOrdrM

logger = logging.getLogger(__name__)

class MainView(View):
    def get(self,request):
        template = loader.get_template("md_main/main.html")
        memid    = request.session.get("memid")
        gid      = request.session.get("gid")
        # logger.debug(memid)
        # logger.debug(gid)

        # 음료
        # tdtos = MdStorM.objects.select_related("menu").filter(menu__dsrt_t=-1).order_by('?')[:5]
        # 음료 메뉴만 필터링하여 상위 5개 결과 가져오기
        drink_orders = MdOrdrM.objects.filter(stor_m__menu__dsrt_t=-1).values('stor_m__menu__menu_id',
                                                                              'stor_m__menu__menu_name',
                                                                              'stor_m__menu__menu_img',).annotate(
            total_orders=Sum('ordr_num')
        ).order_by('-total_orders')[:5]
        
        # 결과 출력
        for item in drink_orders:
            menu_id = item['stor_m__menu__menu_id']
            menu_name = MdMenu.objects.get(menu_id=menu_id).menu_name
            menu_img = item['stor_m__menu__menu_img']
            total_orders = item['total_orders']
            logger.debug(f'[drnk]menu_id:{menu_id}\tmenu_name:{menu_name}\tmenu_img:{menu_img}\ttotal_orders:{total_orders}')
        
        # 디저트
        # ddtos = MdStorM.objects.select_related("menu").filter(menu__drnk_t=-1).order_by('?')[:5]
        # 디저트 메뉴만 필터링하여 상위 5개 결과 가져오기
        dsrt_orders = MdOrdrM.objects.filter(stor_m__menu__drnk_t=-1).values('stor_m__menu__menu_id',
                                                                             'stor_m__menu__menu_name',
                                                                             'stor_m__menu__menu_img',).annotate(
            total_orders=Sum('ordr_num')
        ).order_by('-total_orders')[:5]
        
        # 결과 출력
        for item in dsrt_orders:
            menu_id = item['stor_m__menu__menu_id']
            menu_name = MdMenu.objects.get(menu_id=menu_id).menu_name
            menu_img = item['stor_m__menu__menu_img']
            total_orders = item['total_orders']
            logger.debug(f'[dsrt]menu_id:{menu_id}\tmenu_name:{menu_name}\tmenu_img:{menu_img}\ttotal_orders:{total_orders}')

        # 추천조합
        rdtos = MdComb.objects.annotate(num_c_likes=Count('mdclike')).order_by('-num_c_likes')[:5]
        # logger.debug(f'rdtos : {rdtos}')

        comb_id_list = [rdto.comb_id for rdto in rdtos]
        # logger.debug(f'comb_id_list : {comb_id_list}')
        
        comb_list = MdCombM.objects.select_related('comb', 'menu').filter(comb__comb_id__in=comb_id_list)

        result_dict = {}

        for data in comb_list:
            comb_id   = data.comb.comb_id
            comb_tit  = data.comb.comb_tit
            comb_img  = data.comb.comb_img
            menu_name = data.menu.menu_name
        
            if comb_id not in result_dict:
                result_dict[comb_id] = {'comb_tit': comb_tit, 'comb_img': comb_img, 'menu_names': []}
        
            result_dict[comb_id]['menu_names'].append(menu_name)
            
        # logger.debug(result_dict)
    
        if memid:
            context = {
                "memid":memid,
				"gid" :gid,
                "tdtos":drink_orders,
                "ddtos":dsrt_orders,
                "rdtos":result_dict,
                }
        else:
            context={
                "tdtos":drink_orders,
                "ddtos":dsrt_orders,
                "rdtos":result_dict,
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