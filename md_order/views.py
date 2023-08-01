from django.shortcuts import render, redirect,reverse
from django.views import View
from md_store.models import MdStorM, MdMAlgy, MdAlgyT
from django.http.response import HttpResponseNotFound, HttpResponse
from md_order.models import MdBuck, MdOrdrM, MdOrdr
from django.utils import timezone
from django.template import loader
import logging
from django.db.models import Case, When, Value, CharField


# 로그
logger = logging.getLogger( __name__ )

class OrderInfoView(View):
    def get(self, request):
        user_id = request.session.get('user_id')
        stor_m_id = request.GET.get('stor_m_id')
        bucknum = int(request.GET.get('bucknum', 1))
        storem = MdStorM.objects.get(stor_m_id=stor_m_id)

        algy = MdMAlgy.objects.filter(menu_id=storem.menu_id).first()
        
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
            'dto': storem,
            'stor_m_pric': storem.stor_m_pric,
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


    def post(self, request):
        stor_m_id = request.POST["stor_m_id"]
        storem = MdStorM.objects.get(stor_m_id=stor_m_id)
        algy = MdMAlgy.objects.filter(menu_id=storem.menu_id).first()
        user_id = request.POST['user_id']
        
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
            'algy_n' : algy_n 
        }

        return render(request, 'md_order/orderinfo.html', context)

class CartView(View):
    def post(self, request):
        user_id = request.POST['user_id']
        buck_reg_ts = timezone.now()
        bucknum = int(request.POST["bucknum"])
        stor_m_id = request.POST.get('stor_m_id')

        MdBuck.objects.create(
            user_id=user_id,
            stor_m_id=stor_m_id,
            buck_num=bucknum,
            buck_reg_ts=buck_reg_ts
        )

        # MdStorM 객체를 가져와서 가격을 계산하고 필요한 정보들을 세션에 저장
        storem = MdStorM.objects.get(stor_m_id=stor_m_id)
        buckprice = bucknum * storem.stor_m_pric

        # 필요한 정보들만 딕셔너리로 추출하여 세션에 저장
        cart_data = {
            'stor_m_id': stor_m_id,
            'stor_m_pric': storem.stor_m_pric,
            'stor_id': storem.stor_id,
            'stor_m_name': storem.stor_m_name,
            'bucknum': bucknum,
            'buckprice': buckprice,
            'buck_reg_ts': buck_reg_ts.strftime('%Y-%m-%d %H:%M:%S'), 
        }

        # 세션에 저장
        request.session['cart_data'] = cart_data

        # orderinfo 페이지로 리디렉션
        return redirect(reverse('md_order:orderinfo') + f'?stor_m_id={stor_m_id}')
    
class OrderView(View):
    def post(self, request):
        stor_m_id = request.POST["stor_m_id"]
        user_id = request.POST['user_id']
        bucknum = int(request.POST["bucknum"])
        buck_num = bucknum
        
        buck_reg_ts = timezone.now()
        
        MdBuck.objects.create(
           user_id=user_id,
           stor_m_id=stor_m_id, 
           buck_num=buck_num, 
           buck_reg_ts=buck_reg_ts
           )

        storem = MdStorM.objects.get(stor_m_id=stor_m_id)
        buckprice = bucknum * storem.stor_m_pric
        buck_reg_ts = timezone.now()
        
        if storem.menu_t_id == 0:
            menu_type = "일반"
        else:
            menu_type = "시그니처"
                
        context = {
                'dto': storem,
                'stor_m_pric': storem.stor_m_pric,
                'stor_m_name': storem.stor_m_name,
                'stor_id': storem.stor_id,
                'bucknum': bucknum,
                'buckprice': buckprice,
                'buck_reg_ts' : buck_reg_ts,
            }
        
        return redirect("md_order:buck")

class BuckView(View):
    def get(self, request):
        try:
            stor_m_id = request.POST.get('stor_m_id')
            bucks = MdBuck.objects.select_related('stor_m__stor')
            context = {}

            for buck in bucks:
                store_name = buck.stor_m.stor.stor_name
                buck_price = buck.buck_num * buck.stor_m.stor_m_pric
                buck_del_ts = buck.buck_del_ts
                buck_ord_ts = buck.buck_ord_ts
                user_id = buck.user_id

                if buck_del_ts is None and buck_ord_ts is None:
                    store_data = {
                        'store_id': buck.stor_m.stor.stor_id,
                        'stor_m_name': buck.stor_m.stor_m_name,
                        'stor_m_pric': buck.stor_m.stor_m_pric,
                        'buck_id': buck.buck_id,
                        'buck_num': buck.buck_num,
                        'buck_price': buck_price,
                        'buck_del_ts': buck_del_ts,
                        'buck_ord_ts': buck_ord_ts,
                        'user_id' : user_id
                    }
                    
                    if store_name in context:
                        context[store_name].append(store_data)
                    else:
                        context[store_name] = [store_data]

            logger.debug(f'context : {context}')

            return render(request, 'md_order/buck.html', {'context': context})
        except MdBuck.DoesNotExist:
            return HttpResponseNotFound()
        
        
class BuckDelOrdrView(View):
    def post(self, request):
        selected_bucks = request.POST.getlist('selected_bucks')
        action = request.POST.get('action', None)

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
            if selected_bucks:
                for buck_id in selected_bucks:
                    try:
                        buck = MdBuck.objects.get(pk=buck_id)
                        buck.buck_ord_ts = timezone.now()
                        buck.save()
                        
                        user_id = buck.user_id
                        stor_m_id = buck.stor_m.stor.stor_id
                        buck_num = buck.buck_num
                        weather_id = 0
                        ordr_temp = 0
                        ordr_ord_ts = timezone.now()
                        buck_id = buck.buck_id
                        
                        new_order = MdOrdr.objects.create(
                            user_id=user_id,
                            weather_id=weather_id,
                            ordr_temp=ordr_temp,
                            ordr_ord_ts=ordr_ord_ts,
                            ordr_com_ts=None
                        )
                        ordr_id = new_order.ordr_id
                        ordr_num = buck.buck_num
                    
                        MdOrdrM.objects.create(
                            ordr_id=ordr_id,
                            stor_m_id = buck.stor_m_id,
                            ordr_num = ordr_num
                        )

                    except MdBuck.DoesNotExist:
                        pass
                    
        return redirect('md_order:ordersuc')

class OrdrSucView (View):
    def get(self,request):
        template = loader.get_template( "md_order/ordersuc.html" )
        context = {}
        return HttpResponse( template.render( context, request ) )
    def post(self,request):
        pass


class OrdrListView(View):
    def get(self, request):
        orders = MdOrdr.objects.all()
        
        orders = MdOrdr.objects.annotate(
            order_status=Case(
                When(ordr_com_ts__isnull=True, then=Value('접수완료')),
                default=Value('처리완료'),
                output_field=CharField()
            )
        )

        orders = orders.order_by('order_status', 'ordr_com_ts')
    
        context = []

        for order in orders:
            context_m = []
            order_menus = MdOrdrM.objects.filter(ordr_id=order.ordr_id)
            
            if order.ordr_com_ts is None:
                order_status = '접수완료'
            else:
                order_status = '처리완료'
            
            
            for order_menu in order_menus:
                stor_m = MdStorM.objects.get(stor_m_id=order_menu.stor_m_id)
                context_m.append({
                    'ordr_m_id': order_menu.ordr_m_id,
                    'stor_m_id': order_menu.stor_m_id,
                    'stor_m_name': stor_m.stor_m_name,
                    'ordr_num': order_menu.ordr_num,
                })

            
            
            
                context.append({
                        'ordr_id': order.ordr_id,
                        'user_id': order.user_id,
                        'weather_id': order.weather_id,
                        'weather_name': order.weather.weather_name,
                        'ordr_temp': order.ordr_temp,
                        'ordr_ord_ts': order.ordr_ord_ts,
                        'ordr_com_ts': order.ordr_com_ts,
                        'stor_m_name': stor_m.stor_m_name,
                        'order_status': order_status,  
                        'order_menus': context_m,
                    })
        


        return render(request, 'md_order/orderlist.html', {'context': context})
    

class OrdrDoneView (View):
    def post(self, request):
        ordr_id = request.POST.get('ordr_id')
        try:
            ordr = MdOrdr.objects.get(pk=ordr_id)
            if ordr.ordr_com_ts is None:
                ordr.ordr_com_ts = timezone.now()
                ordr.save()
        except MdOrdr.DoesNotExist:
            pass
        return redirect('md_order:orderlist')