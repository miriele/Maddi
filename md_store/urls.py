from django.urls.conf import path
from md_store import views

app_name = "md_store"

urlpatterns = [
         path("store",          views.StoreView.as_view(),          name="store"),
         path("imagestore",     views.ImageStoreView.as_view(),     name="imagestore"),
         path("menuinfo",       views.MenuInfoView.as_view(),       name="menuinfo"),
         path("menulist",       views.MenuListView.as_view(),       name="menulist"),
         path("addmenu",        views.AddMenuView.as_view(),        name="addmenu"),
         path("storeuser",      views.StoreUserView.as_view(),      name="storeuser"),
         path("addjumju",       views.AddJumjuView.as_view(),       name="addjumju"),
         path("mypagejumju",    views.MypageJumjuView.as_view(),    name="mypagejumju"),
    ]
