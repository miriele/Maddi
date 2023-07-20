from django.shortcuts import render
from django.views import View
from md_store.models import MdStorM
from django.http.response import HttpResponseNotFound
from md_order.models import MdBuck

class OrderInfoView(View):
    def get(self, request):
        stor_m_id = 141
        bucknum = 1
        
        try:
            storem = MdStorM.objects.get(stor_m_id=stor_m_id)

            if storem.menu_t_id == 0:
                menu_type = "일반"
            else:
                menu_type = "시그니처"
            stor_m = MdStorM.objects.get(stor_m_id=stor_m_id)
            stor_m_pric = storem.stor_m_pric
            buckprice = bucknum * stor_m_pric
            
            context = {
                'dto': storem,
                'stor_m_pric': stor_m_pric,
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
        stor_m_id = 141
        bucknum = int(request.POST.get('bucknum', 1))  # 기본값 1

        try:
            storem = MdStorM.objects.get(stor_m_id=stor_m_id)

            if storem.menu_t_id == 0:
                menu_type = "일반"
            else:
                menu_type = "시그니처"
            stor_m = MdStorM.objects.get(stor_m_id=stor_m_id)

            # 주문 수량이 0 이하일 때 1로 설정
            if bucknum <= 0:
                bucknum = 1
                context = {
                    'dto': storem,
                    'stor_m_pric': storem.stor_m_pric,
                    'stor_m_name': storem.stor_m_name,
                    'stor_m_cal': storem.stor_m_cal,
                    'stor_m_info': storem.stor_m_info,
                    'stor_m_img': storem.stor_m_img,
                    'menu_type': menu_type,
                    'bucknum': bucknum,
                    'error_message': '최소 주문 수량은 1개 이상입니다.',
                }
                return render(request, 'md_order/orderinfo.html', context)

            context = {
                'dto': storem,
                'stor_m_pric': storem.stor_m_pric,
                'stor_m_name': storem.stor_m_name,
                'stor_m_cal': storem.stor_m_cal,
                'stor_m_info': storem.stor_m_info,
                'stor_m_img': storem.stor_m_img,
                'menu_type': menu_type,
                'bucknum': bucknum,
            }

            return render(request, 'md_order/orderinfo.html', context)

        except MdStorM.DoesNotExist:
            return HttpResponseNotFound()
    