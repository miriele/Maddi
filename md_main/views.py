from django.db.models.aggregates import Count, Sum
from django.db.models import F
from django.http.response import HttpResponse
from django.template import loader
from django.utils.decorators import method_decorator
from django.utils import timezone
from django.views.generic.base import View
from django.views.decorators.csrf import csrf_exempt
from md_admin.models import MdSrch
from md_combi.models import MdCombM, MdComb
from md_order.models import MdOrdrM
from md_store.models import MdStorM, MdStor, MdMenu, MdBjd
import logging

logger = logging.getLogger(__name__)

class MainView(View):
    def get(self,request):
        template = loader.get_template("md_main/main.html")
        memid    = request.session.get("memid")
        gid      = request.session.get("gid")
        # logger.debug(memid)
        # logger.debug(gid)

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
        logger.debug(f'memid : {memid}')
    
        if memid:
            context = {
                "memid" :memid,
				"gid"   :gid,
                "tdtos" :drink_orders,
                "ddtos" :dsrt_orders,
                "rdtos" :result_dict,
                }
        else:
            context={
                "tdtos" :drink_orders,
                "ddtos" :dsrt_orders,
                "rdtos" :result_dict,
                }
        return HttpResponse(template.render(context,request))

    def post(self,request):
        pass


class SearchView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return View.dispatch(self, request, *args, **kwargs)    

    def post(self, request):
        template   = loader.get_template("md_main/searchlist.html")
        searchText = request.POST["searchword"]
        bjdName    = request.POST["bjd_name"]
        
        logger.debug(f'searchText : {searchText}\tbjdName : {bjdName}')
        
        subquery_sb = MdStorM.objects.filter(
                            menu__menu_name=searchText
                        ).values('stor_id').distinct()
    
        store_list  = MdStor.objects.filter(
                            bjd_code__bjd_name=bjdName,
                            area_t_id__in=MdStor.objects.filter(
                                bjd_code__bjd_name=bjdName
                            ).values('area_t_id')
                        ).annotate(
                            area_t_name=F('area_t__area_t_name')
                        ).filter(
                            stor_id__in=subquery_sb
                        ).values(
                            'stor_id',
                            'stor_name',
                            'stor_img',
                            'area_t_name'
                        )
        
        logger.debug(f'store_list: {store_list}')
        logger.debug(f'store_cnt: {len(store_list)}')
        
        user_id = request.session.get("memid")
        # bjd_code = MdBjd.objects.filter(bjd_name=bjdName).values('bjd_code').first()['bjd_code']
        bjd_code = MdBjd.objects.filter(bjd_name=bjdName).first()
        logger.debug(f'user_id  : {user_id}')
        logger.debug(f'bjd_code : {bjd_code}')
        # logger.debug(f'srch_ts  : {timezone.localtime()}')
        logger.debug(f'srch_ts  : {timezone.now()}')
        
        searchInfo = MdSrch(
            user_id   = user_id,
            bjd_code  = bjd_code,
            srch_word = searchText,
            srch_ts   = timezone.now(),
            )
        searchInfo.save()

        context = {
            "store_list" : store_list,
            "count" : len(store_list),
            }
        return HttpResponse(template.render(context, request))

class MapView(View):
    def get(self, request):
        template = loader.get_template("md_main/map.html")
        # addr = request.GET("centerAddr")
        # print(addr) 
        context = {}
        return HttpResponse(template.render(context,request))

import json
class SearchWord(View):
    @method_decorator( csrf_exempt )
    def dispatch(self, request, *args, **kwargs):
        return View.dispatch(self, request, *args, **kwargs)

    def post(self, request):
        search_word = request.POST["search_word"]
        queryset    = MdMenu.objects.filter(menu_name__contains=search_word)[:10]
        menulist    = [menu.menu_name for menu in queryset]
        menudict    = dict(zip(range(0, len(menulist)), menulist))
        # logger.debug(f'menudict: {json.dumps(menudict)}')
        return HttpResponse(json.dumps(menudict), content_type ="application/json")
        