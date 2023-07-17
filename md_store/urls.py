from django.urls.conf import path
from md_store import views

app_name = "md_store"

urlpatterns = [
         path( "store", views.StoreView.as_view(), name="store" ),
         path( "menu", views.MenuView.as_view(), name="menu" ),
         path("image", views.ImageView.as_view(), name="image"),
       ]