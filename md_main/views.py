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
from md_store.models import MdStorM, MdStor, MdMenu, MdBjd, MdRecommend
import json
import logging

logger = logging.getLogger(__name__)

class MainView(View):
    def get(self, request):
        template = loader.get_template("md_main/main.html")
        memid    = request.session.get("memid")
        gid      = request.session.get("gid")
        # logger.debug(memid)
        # logger.debug(gid)
        
        # 고객 맞춤 메뉴 추천
        check_id = MdRecommend.objects.filter(user=memid).count()
        rec_count = MdRecommend.objects.count()
        # 추천테이블 user_id확인
        if(memid):
            if(check_id !=0):
                print(memid,"추천테이블에 있는아이디")
                recom_drnk = MdRecommend.objects.filter(user=memid,menu__dsrt_t=-1).values('menu__menu_id','menu__menu_name','menu__menu_img')
                recom_dsrt = MdRecommend.objects.filter(user=memid,menu__drnk_t=-1).values('menu__menu_id','menu__menu_name','menu__menu_img')
            else:
                # 문자열 -> 리스트
                noexid = list(memid)
                strtoint = []
                # 문자 -> 아스키코드
                for i in noexid:
                    asci_code = ord(i)
                    strtoint.append(asci_code)
                # 아스키코드값 합
                recom_id = sum(strtoint)    
                recom_id = (recom_id + rec_count) % rec_count
                change_id = MdRecommend.objects.filter(reco_id=recom_id).values("user")
                change_id = list(change_id)
                change_id = change_id[0]['user']                    
                recom_drnk=MdRecommend.objects.filter(user=change_id,menu__dsrt_t=-1).values('menu__menu_id','menu__menu_name','menu__menu_img')
                recom_dsrt=MdRecommend.objects.filter(user=change_id,menu__drnk_t=-1).values('menu__menu_id','menu__menu_name','menu__menu_img')
        
            for item in recom_drnk:
                menu_id = item['menu__menu_id']
                menu_name = MdMenu.objects.get(menu_id=menu_id).menu_name
                menu_img = item['menu__menu_img']
            
            for item in recom_dsrt:
                menu_id = item['menu__menu_id']
                menu_name = MdMenu.objects.get(menu_id=menu_id).menu_name
                menu_img = item['menu__menu_img']

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
            # logger.debug(f'[drnk]menu_id:{menu_id}\tmenu_name:{menu_name}\tmenu_img:{menu_img}\ttotal_orders:{total_orders}')
        
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
            # logger.debug(f'[dsrt]menu_id:{menu_id}\tmenu_name:{menu_name}\tmenu_img:{menu_img}\ttotal_orders:{total_orders}')

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
        # logger.debug(f'memid : {memid}')
    
        if memid:
            context = {
                "memid"     :memid,
				"gid"       :gid,
                "tdtos"     :drink_orders,
                "ddtos"     :dsrt_orders,
                "rdtos"     :result_dict,
                "recom_drnk":recom_drnk,
                "recom_dsrt":recom_dsrt
                }
        else:
            context={
                "tdtos" :drink_orders,
                "ddtos" :dsrt_orders,
                "rdtos" :result_dict,
                }
        return HttpResponse(template.render(context,request))


class SearchView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return View.dispatch(self, request, *args, **kwargs)    

    def post(self, request):
        searchText   = request.POST["search_word"]
        bjdName      = request.POST["bjd_name"]
        strLatiSouth = request.POST["latiSouth"]
        strLatiNorth = request.POST["latiNorth"]
        strLongWest  = request.POST["longWest"]
        strLongEast  = request.POST["longEast"]
        # logger.debug(f'searchText : {searchText}\tbjdName : {bjdName}')
        # logger.debug(f'strLatiSouth : {strLatiSouth}\tstrLatiNorth : {strLatiNorth}')
        # logger.debug(f'strLongWest : {strLongWest}\tstrLongEast : {strLongEast}')
        # logger.debug(f'type(strLatiSouth) : {type(strLatiSouth)}\tfloat(strLatiSouth) : {float(strLatiSouth)}')
        
        subquery_sb = MdStorM.objects.filter(
                            menu__menu_name=searchText
                        ).values('stor_id').distinct()
    
        store_list  = MdStor.objects.filter(
                            bjd_code__bjd_name=bjdName,
                            area_t_id__in=MdStor.objects.filter(
                                bjd_code__bjd_name=bjdName
                            ).values('area_t_id'),
                            stor_lati__gt=float(strLatiSouth),
                            stor_lati__lt=float(strLatiNorth),
                            stor_long__gt=float(strLongWest),
                            stor_long__lt=float(strLongEast)
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
        # logger.debug(f'store_list: {store_list}')
        # logger.debug(f'store_cnt: {len(store_list)}')
        
        user_id  = request.session.get("memid")
        bjd_code = MdBjd.objects.filter(bjd_name=bjdName).first()
        # logger.debug(f'user_id  : {user_id}')
        # logger.debug(f'bjd_code : {bjd_code}')
        # logger.debug(f'srch_ts  : {timezone.now()}')
        
        searchInfo = MdSrch(
            user_id   = user_id,
            bjd_code  = bjd_code,
            srch_word = searchText,
            srch_ts   = timezone.now(),
            )
        searchInfo.save()

        context = {
            "menu_name"  : searchText,
            "count"      : len(store_list),
            "store_list" : list(store_list),
            }
        return HttpResponse(json.dumps(context), content_type="application/json")


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
        return HttpResponse(json.dumps(menudict), content_type="application/json")
        