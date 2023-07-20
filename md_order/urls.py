from django.urls.conf import path
from md_order import views

app_name = "md_order"

urlpatterns = [
         path( "orderinfo", views.OrderInfoView.as_view(), name="orderinfo" ),
         path( "cart", views.CartView.as_view(), name="cart" ),
         path( "order", views.OrderView.as_view(), name="order" ),
         path( "buck", views.BuckView.as_view(), name="buck" ),
       ]




