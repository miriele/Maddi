from django.db.models import Case, When, Value, CharField
from django.http.response import HttpResponseNotFound, HttpResponse
from django.shortcuts import render, redirect,reverse
from django.template import loader
from django.utils import timezone
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from md_store.models import MdStorM, MdMAlgy, MdAlgyT, MdStor, MdBh
from md_order.models import MdBuck, MdOrdrM, MdOrdr
import logging
import requests
import xmltodict
from django.db.models import F
import json

# 로그
logger = logging.getLogger( __name__ )

class OrderInfoView(View):
    def get(self, request):
        user_id   = request.session.get('memid')
        memid     = request.session.get('memid')
        gid       = request.session.get("gid")
        stor_id   = request.GET.get('stor_id')
        stor_m_id = request.GET.get('stor_m_id')
        bucknum   = int(request.GET.get('bucknum', 1))
        storem    = MdStorM.objects.get(stor_m_id=stor_m_id)
        algy      = MdMAlgy.objects.filter(menu_id=storem.menu_id).first()
        stor      = MdStor.objects.get(stor_id = stor_id)
        jumju     = stor.user_id
        
        if algy is not None:
            algyn = MdAlgyT.objects.get(algy_t_id=algy.algy_t_id)
            if algyn.algy_t_name is not None:
                algy_n = algyn.algy_t_name
        else:
            algy_n = "없음"

        
        if storem.menu_t_id == 0:
            menu_type = "일반"
        else:
            menu_type = "시그니처"

        buckprice = bucknum * storem.stor_m_pric

        context = {
            "memid"       : memid,
            'dto'         : storem,
            'stor_m_pric' : storem.stor_m_pric,
            'stor_m_name' : storem.stor_m_name,
            'stor_m_cal'  : storem.stor_m_cal,
            'stor_m_info' : storem.stor_m_info,
            'stor_m_img'  : storem.stor_m_img,
            'menu_type'   : menu_type,
            'bucknum'     : bucknum,
            'buckprice'   : buckprice,
            'stor_id'     : stor_id,
            'stor_m_id'   : stor_m_id,
            'algy_n'      : algy_n,
            'user_id'     : user_id,
            'gid'         : gid,
            'jumju'       : jumju,
        }

        return render(request, 'md_order/orderinfo.html', context)

    def post(self, request):
        stor_m_id = request.POST["stor_m_id"]
        storem = MdStorM.objects.get(stor_m_id=stor_m_id)
        algy = MdMAlgy.objects.filter(menu_id=storem.menu_id).first()
        user_id = request.session.get('memid')
        
        if algy is not None:
            algyn = MdAlgyT.objects.get(algy_t_id=algy.algy_t_id)
            if algyn.algy_t_name is not None:
                algy_n = algyn.algy_t_name
        else:
            algy_n = "없음"

        if storem.menu_t_id == 0:
            menu_type = "일반"
        else:
            menu_type = "시그니처"
            
        bucknum = int(request.POST.get('bucknum', 1))
         
        if bucknum <= 0:
            bucknum = 1

        buckprice = bucknum * storem.stor_m_pric
        
        
        context = {
            'dto': storem,
            'stor_m_pric': storem.stor_m_pric,
            'stor_id': storem.stor_id,
            'stor_m_name': storem.stor_m_name,
            'stor_m_cal': storem.stor_m_cal,
            'stor_m_info': storem.stor_m_info,
            'stor_m_img': storem.stor_m_img,
            'menu_type': menu_type,
            'bucknum': bucknum,
            'buckprice': buckprice,
            'stor_m_id' : stor_m_id,
            'algy_n' : algy_n,
            'user_id' :user_id 
        }

        return render(request, 'md_order/orderinfo.html', context)

class CartView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return View.dispatch(self, request, *args, **kwargs)
    
    def post(self, request):
        user_id     = request.POST['user_id']
        buck_reg_ts = timezone.now()
        bucknum     = int(request.POST["buck_num"])
        stor_m_id   = request.POST.get('stor_m_id')
        stor_id     = request.POST.get('stor_id')

        # logger.debug(f'bucknum : {bucknum}\tstor_m_id : {stor_m_id}\tstor_id : {stor_id}')

        MdBuck.objects.create(
            user_id=user_id,
            stor_m_id=stor_m_id,
            buck_num=bucknum,
            buck_reg_ts=buck_reg_ts
        )

        # MdStorM 객체를 가져와서 가격을 계산하고 필요한 정보들을 세션에 저장
        storem    = MdStorM.objects.get(stor_m_id=stor_m_id)
        buckprice = bucknum * storem.stor_m_pric

        # 필요한 정보들만 딕셔너리로 추출하여 세션에 저장
        cart_data = {
            'stor_m_id'     : stor_m_id,
            'stor_m_pric'   : storem.stor_m_pric,
            'stor_id'       : storem.stor_id,
            'stor_m_name'   : storem.stor_m_name,
            'bucknum'       : bucknum,
            'buckprice'     : buckprice,
            'buck_reg_ts'   : buck_reg_ts.strftime('%Y-%m-%d %H:%M:%S'), 
        }

        # 세션에 저장
        request.session['cart_data'] = cart_data

        # orderinfo 페이지로 리디렉션
        return redirect(reverse('md_store:storeuser') + f'?stor_id={stor_id}')
    
class OrderView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return View.dispatch(self, request, *args, **kwargs)
    
    def post(self, request):
        stor_m_id   = request.POST["stor_m_id"]
        user_id     = request.POST['user_id']
        bucknum     = int(request.POST["ordr_num"])
        buck_num    = bucknum
        buck_reg_ts = timezone.now()
        
        MdBuck.objects.create(
           user_id      = user_id,
           stor_m_id    = stor_m_id, 
           buck_num     = buck_num, 
           buck_reg_ts  = buck_reg_ts
           )

        storem = MdStorM.objects.get(stor_m_id=stor_m_id)
        
        return redirect("md_order:buck")

class BuckView(View):
    def get(self, request):
        try:
            memid   = request.session.get('memid')
            gid     = request.session.get('gid')
            user_id = request.session.get("memid")
            bucks   = MdBuck.objects.select_related('stor_m__stor').filter(user_id=user_id)
            context = {}

            for buck in bucks:
                store_name  = buck.stor_m.stor.stor_name
                buck_price  = buck.buck_num * buck.stor_m.stor_m_pric
                buck_del_ts = buck.buck_del_ts
                buck_ord_ts = buck.buck_ord_ts
                user_id     = buck.user_id

                if buck_del_ts is None and buck_ord_ts is None:
                    store_data = {
                        'store_id'   : buck.stor_m.stor.stor_id,
                        'bjd_code'   : buck.stor_m.stor.bjd_code.bjd_code,
                        'stor_m_name': buck.stor_m.stor_m_name,
                        'stor_m_pric': buck.stor_m.stor_m_pric,
                        'buck_id'    : buck.buck_id,
                        'buck_num'   : buck.buck_num,
                        'buck_price' : buck_price,
                        'buck_del_ts': buck_del_ts,
                        'buck_ord_ts': buck_ord_ts,
                        'user_id'    : user_id
                    }
                    
                    if store_name in context:
                        context[store_name].append(store_data)
                    else:
                        context[store_name] = [store_data]

            logger.debug(f'context : {context}')

            return render(request, 'md_order/buck.html', {'context': context, 'memid' : memid, 'gid':gid})
        except MdBuck.DoesNotExist:
            return HttpResponseNotFound()


def forecast(url, params):
    # 값 요청 (웹 브라우저 서버에서 요청 - url주소와 파라미터)
    res = requests.get(url, params = params)

    #XML -> 딕셔너리
    xml_data  = res.text
    dict_data = xmltodict.parse(xml_data)

    #값 가져오기
    weather_data = dict()
    for item in dict_data['response']['body']['items']['item']:
        # 기온
        if item['category'] == 'T1H':
            weather_data['tmp'] = item['fcstValue']
        # 습도
        if item['category'] == 'REH':
            weather_data['hum'] = item['fcstValue']
        # 하늘상태: 맑음(1) 구름많은(3) 흐림(4)
        if item['category'] == 'SKY':
            weather_data['sky'] = item['fcstValue']
        # 강수형태: 없음(0), 비(1), 비/눈(2), 눈(3), 빗방울(5), 빗방울눈날림(6), 눈날림(7)
        if item['category'] == 'PTY':
            weather_data['sky2'] = item['fcstValue']

    return weather_data


class BuckDelOrdrView(View):
    def post(self, request):
        selected_bucks = request.POST.getlist('selected_bucks')
        action         = request.POST.get('action', None)

        if action == '선택삭제':
            if selected_bucks:
                for buck_id in selected_bucks:
                    try:
                        buck = MdBuck.objects.get(pk=buck_id)
                        buck.buck_del_ts = timezone.now()
                        buck.save()
                    except MdBuck.DoesNotExist:
                        pass
                    
                return redirect('md_order:buck')
                    
        elif action == '주문하기':
            memid    = request.session.get('memid')
            curtime  = timezone.now()
            strDate  = curtime.strftime('%Y%m%d')
            bjd_code = int(request.POST['bjd_code'])
            logger.debug(f'bjd_code:{bjd_code}\ttype(bjd_code) : {type(bjd_code)}')

            if curtime.minute < 45:
                if curtime.hour == 0:
                    strTime = "2330"
                else:
                    pre_hour = curtime.hour-1
                    if pre_hour < 10:
                        strTime = "0" + str(pre_hour) + "30"
                    else:
                        strTime = str(pre_hour) + "30"
            else:
                if curtime.hour < 10:
                    strTime = "0" + str(curtime.hour) + "30"
                else:
                    strTime = str(curtime.hour) + "30"

            # get position (nx, ny)
            # 값을 얻어오지 못할 경우, 서울 서초구를 기본 좌표로 준다
            nx = 61
            ny = 125
            try:
                bh_entries  = MdBh.objects.filter(bjd_code=bjd_code)
                hjd_objects = [bh.hjd_code for bh in bh_entries]
            
                nx = [hjd.hjd_x for hjd in hjd_objects][0]
                ny = [hjd.hjd_y for hjd in hjd_objects][0]
                
                print("hjd_x values:", nx)
                print("hjd_y values:", ny)
            except MdBh.DoesNotExist:
                logger.debug("MdBh instance with bjd_code not found")
            
            logger.debug(f'nx : {nx}\tny : {ny}')
            
            # get weather info.
            # keys   = 'HWhDUnifun4TFn7nZAJYjxhrrqE20%2Fn3%2BvsK7BFCdbesAK9K7wiOBsYkYztAqmlAbVu%2FkZSeE6lyNCcq4DmK%2Bw%3D%3D'
            keys   = 'HWhDUnifun4TFn7nZAJYjxhrrqE20/n3+vsK7BFCdbesAK9K7wiOBsYkYztAqmlAbVu/kZSeE6lyNCcq4DmK+w=='
            url    = 'http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getUltraSrtFcst'
            params ={'serviceKey' : keys,
                     'pageNo'     : '1',
                     'numOfRows'  : '1000',
                     'dataType'   : 'XML',
                     'base_date'  : strDate,
                     'base_time'  : strTime,
                     'nx'         : nx,
                     'ny'         : ny }
            
            dict_sky    = forecast(url, params)
            weather_id  = 0
            ordr_temp   = 0
            
            logger.debug(f'dict_sky : {dict_sky}')

            if dict_sky['sky2'] == '0' :
                if dict_sky['sky'] == '1' :
                    weather_id = 0
                elif dict_sky['sky'] == '3' :
                    weather_id = 1
                elif dict_sky['sky'] == '4' :
                    weather_id = 2
            elif dict_sky['sky2'] == '1' :
                weather_id = 3
            elif dict_sky['sky2'] == '2' :
                weather_id = 3
            elif dict_sky['sky2'] == '3' :
                weather_id = 4
            elif dict_sky['sky2'] == '5' :
                weather_id = 3
            elif dict_sky['sky2'] == '6' :
                weather_id = 3
            elif dict_sky['sky2'] == '7' :
                weather_id = 4
            else :
                weather_id = 0
            
            if dict_sky['tmp'] != None:
                ordr_temp = int(dict_sky['tmp'])

            logger.debug(f'weather_id : {weather_id}\tordr_temp : {ordr_temp}')

            new_order = MdOrdr.objects.create(
                user_id     = memid,
                weather_id  = weather_id,
                ordr_temp   = ordr_temp,
                ordr_ord_ts = curtime,
                ordr_com_ts = None
            )
            
            ordr_id  = new_order.ordr_id

            if selected_bucks:
                for buck_id in selected_bucks:
                    buck = MdBuck.objects.get(pk=buck_id)
                    buck.buck_ord_ts = curtime
                    buck.save()
                    
                    MdOrdrM.objects.create(
                        ordr_id     = ordr_id,
                        stor_m_id   = buck.stor_m_id,
                        ordr_num    = buck.buck_num
                    )
                    
        return redirect('md_order:ordersuc')

class OrdrSucView (View):
    def get(self,request):
        template = loader.get_template( "md_order/ordersuc.html" )
        memid   = request.session.get('memid')
        gid     = request.session.get('gid')
        context = {
            "memid" : memid,
            "gid"   : gid,   
            }
        return HttpResponse( template.render( context, request ) )


class OrdrListView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return View.dispatch(self, request, *args, **kwargs)
    def get(self, request):
        
        memid   = request.session.get("memid")
        gid     = request.session.get("gid")
        
        stor_id = request.GET['stor_id']
        
        #데이터 있나 없나 확인용 count
        count = MdOrdr.objects.select_related('mdordrm__stor_m', 'user').filter(mdordrm__stor_m__stor_id = stor_id, ordr_com_ts = None ).count()
        logger.debug(f' count : { count }')
        
        odtos   = MdOrdr.objects.select_related('mdordrm__stor_m', 'user'
                ).filter(mdordrm__stor_m__stor_id = stor_id, ordr_com_ts = None 
                    ).values(
                        'ordr_id', 'user__user_nick', 'mdordrm__ordr_num', 
                        'mdordrm__stor_m__stor_m_name', 'ordr_ord_ts', 'ordr_com_ts'
                        ).order_by("-ordr_id").annotate(
                            user_name   = F('user__user_nick'),
                            ordr_num    = F('mdordrm__ordr_num'),
                            menu_name   = F('mdordrm__stor_m__stor_m_name'),
                            ordr_ts     = F('ordr_ord_ts'),
                            com_ts      = F('ordr_com_ts'),
                            )
        # logger.debug(f' odtos : { odtos }')
        ordr_l = dict()
        
        for o in odtos :
            order_id = o["ordr_id"]
            
            if order_id not in ordr_l :
                ordr_l[order_id] = {
                    "user_name" : o["user_name"],
                    "ordr_num"  : [],
                    "menu_name" : [],
                    "ordr_ts"   : o["ordr_ts"],
                    "com_ts"    : o["com_ts"],
                    }
            ordr_l[order_id]["menu_name"].append(o["menu_name"]) 
            ordr_l[order_id]["ordr_num"].append(o["ordr_num"])     
        
        template = loader.get_template("md_order/orderlist.html")
        context = {
            "count"     : count,
            "ordr_l"    : ordr_l,
            "stor_id"   : stor_id,
            "memid"     : memid,
            "gid"       : gid,
        }
        
        return HttpResponse(template.render(context, request))
    
    def post(self, request):
        
        ordr_id_temp = request.POST.get("ordr_id","")
        ordr_id = ordr_id_temp.split('_')[-1]
        logger.debug(f'ordr_id : {ordr_id} ')
        
        ordr = MdOrdr.objects.get(ordr_id = ordr_id )
        logger.debug(f'ordr : {ordr.user_id} ')
        
        comTime = timezone.now()
        
        ordr.ordr_com_ts = comTime
        ordr.save()
        
        context = {
            "comTime" : comTime.strftime("%Y년 %m월 %d일 %H:%M:%S"),
            "ordr_id" : ordr_id,
            }
        logger.debug(f'context : {context} ')
        
        return HttpResponse(json.dumps(context), content_type="application/json")
    
