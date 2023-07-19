from django.urls.conf import path
from md_store import views

app_name = "md_store"

urlpatterns = [
         path( "store", views.StoreView.as_view(), name="store" ),
         path("image", views.ImageView.as_view(), name="image"),
         path("menuinfo", views.MenuInfoView.as_view(), name="menuinfo"),
         path("menulist", views.MenuListView.as_view(), name="menulist"),
         path("addmenu", views.AddMenuView.as_view(), name="addmenu"),
       ]

