from django.urls.conf import path
from md_order import views

app_name = "md_order"

urlpatterns = [
         path( "orderinfo", views.OrderInfoView.as_view(), name="orderinfo" ),
       ]

