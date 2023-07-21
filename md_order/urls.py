from django.urls.conf import path
from md_order import views

app_name = "md_order"

urlpatterns = [
         path( "orderinfo", views.OrderInfoView.as_view(), name="orderinfo" ),
         path( "cart", views.CartView.as_view(), name="cart" ),
         path( "order", views.OrderView.as_view(), name="order" ),
         path( "buck", views.BuckView.as_view(), name="buck" ),
         
         path( "buckdel", views.BuckDelView.as_view(), name="buckdel" ),
         path( "buckordr", views.BuckOrdrView.as_view(), name="buckordr" ),
         path( "buckordr", views.BuckOrdrView.as_view(), name="buckordr" ),
         path( "orderlist", views.OrdrListView.as_view(), name="orderlist" ),
         path( "ordersuc", views.OrdrSucView.as_view(), name="ordersuc" ),
         path( "orderalert", views.OrdrAlertView.as_view(), name="orderalert" ),
         path( "orderdone", views.OrdrDoneView.as_view(), name="orderdone" ),
       ]

