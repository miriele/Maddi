from django.shortcuts import render, redirect
from django.views import View
from md_store.models import MdStorM
from django.http.response import HttpResponseNotFound, HttpResponse
from md_order.models import MdBuck, MdOrdrM, MdOrdr
from django.utils.dateformat import DateFormat
from django.utils import timezone
from django.template import loader
import logging
import md_order

# 로그
logger = logging.getLogger( __name__ )

class OrderInfoView(View):
    def get(self, request):
        stor_m_id = 37957
        bucknum = int(request.GET.get('bucknum', 1))  # 기본값 1

        try:
            storem = MdStorM.objects.get(stor_m_id=stor_m_id)

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
            }

            return render(request, 'md_order/orderinfo.html', context)

        except MdStorM.DoesNotExist:
            return HttpResponseNotFound()

    def post(self, request):
        stor_m_id = 37957

        try:
            storem = MdStorM.objects.get(stor_m_id=stor_m_id)
            bucknum = int(request.POST.get('bucknum', 1))  # 기본값 1

            if storem.menu_t_id == 0:
                menu_type = "일반"
            else:
                menu_type = "시그니처"

            # 주문 수량이 0 이하일 때 1로 설정
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
            }

            return render(request, 'md_order/orderinfo.html', context)

        except MdStorM.DoesNotExist:
            return HttpResponseNotFound()

class CartView(View):
    def post(self, request):
        stor_m_id = request.POST["stor_m_id"]
        user_id = "abc001" # 추후에 세션에서 받음 
        bucknum = int(request.POST["bucknum"])
        buck_num = bucknum
        
        # buck_reg_ts에 현재 시각 저장
        buck_reg_ts = timezone.now()
        
        new_buck = MdBuck.objects.create(user_id=user_id, stor_m_id=stor_m_id, buck_num=buck_num, buck_reg_ts=buck_reg_ts)
        buck_id = 60
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
                'stor_id': storem.stor_id,
                'stor_m_name': storem.stor_m_name,
                'buck_id' : buck_id,
                'bucknum': bucknum,
                'buckprice': buckprice,
                'buck_reg_ts' : buck_reg_ts,
            }
        
        return redirect("md_order:orderinfo")

    
class OrderView(View):
    def post(self, request):
        stor_m_id = request.POST["stor_m_id"]
        user_id = "abc001" # 추후에 세션에서 받음 
        bucknum = int(request.POST["bucknum"])
        buck_num = bucknum
        
        # buck_reg_ts에 현재 시각 저장
        buck_reg_ts = timezone.now()
        new_buck = MdBuck.objects.create(user_id=user_id, stor_m_id=stor_m_id, buck_num=buck_num, buck_reg_ts=buck_reg_ts)
        buck_id = 60
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
                'buck_id' : buck_id,
                'stor_id': storem.stor_id,
                'bucknum': bucknum,
                'buckprice': buckprice,
                'buck_reg_ts' : buck_reg_ts,
            }
        
        return redirect("md_order:buck")

class BuckView(View):
    def get(self, request):
        try:
            bucks = MdBuck.objects.select_related('stor_m__stor')
            context = {}

            for buck in bucks:
                store_name = buck.stor_m.stor.stor_name
                store_data = {
                        # 'dto'        : buck.stor_m,
                        'store_id'   : buck.stor_m.stor.stor_id,
                        'stor_m_name': buck.stor_m.stor_m_name,
                        'stor_m_pric': buck.stor_m.stor_m_pric,
                        # 'buck_id'    : buck.buck_id,
                        'buck_num'   : buck.buck_num,
                        'buck_price' : buck.buck_num * buck.stor_m.stor_m_pric,
                        # 'buck_reg_ts': buck.buck_reg_ts,
                    }
                
                if store_name in context :
                    context[store_name].append(store_data)
                else :
                    context[store_name] = [store_data]
            
            logger.debug(f'context : {context}')

            return render(request, 'md_order/buck.html', {'context': context})
        except MdBuck.DoesNotExist:
            return HttpResponseNotFound()

class BuckDelView(View):
    def post(self, request):
        selected_bucks = request.POST.getlist('selected_bucks')
        MdBuck.objects.filter(buck_id__in=selected_bucks, buck_del_ts__isnull=True).update(buck_del_ts=timezone.now())
        
        return redirect('md_order:buck')



class BuckOrdrView (View):
    def get(self,request):
        template = loader.get_template( "md_order/buck.html" )
        context = {}
        return HttpResponse( template.render( context, request ) )
    def post(self,request):
        pass

class OrdrSucView (View):
    def get(self,request):
        template = loader.get_template( "md_order/ordersuc.html" )
        context = {}
        return HttpResponse( template.render( context, request ) )
    def post(self,request):
        pass

class OrdrListView(View):
    def get(self, request):
        template = loader.get_template("md_order/orderlist.html")
        ordrs = MdOrdr.objects.all()
        buck = MdBuck.objects.all()
        storem = MdStorM.objects.all()
        ordrm = MdOrdrM.objects.all()
        context = []
        
        for ordr in ordrs:
            
            if buck:
                    context.append({
                    'ordr_id': ordr.ordr_id,
                    'user_nick': ordr.user.user_nick,
                
                })

        return HttpResponse(template.render({'context': context}, request))

    def post(self, request):
        pass




class OrdrAlertView (View):
    def get(self,request):
        template = loader.get_template( "md_order/orderlist.html" )
        context = {}
        return HttpResponse( template.render( context, request ) )
    def post(self,request):
        pass

class OrdrDoneView (View):
    def get(self,request):
        template = loader.get_template( "md_order/orderdone.html" )
        context = {}
        return HttpResponse( template.render( context, request ) )
    def post(self,request):
        pass


















