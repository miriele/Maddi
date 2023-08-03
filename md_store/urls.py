from django.urls.conf import path
from md_store import views

app_name = "md_store"

urlpatterns = [
         path("store",          views.StoreView.as_view(),          name="store"),
         path("menuinfo",       views.MenuInfoView.as_view(),       name="menuinfo"),
         path("addmenu",        views.AddMenuView.as_view(),        name="addmenu"),
         path("storeuser",      views.StoreUserView.as_view(),      name="storeuser"),
         path("addjumju",       views.AddJumjuView.as_view(),       name="addjumju"),
         path("addjumjusuc",    views.AddJumjuSucView.as_view(),    name="addjumjusuc"),
         path("addmenusuc",     views.AddMenuSucView.as_view(),     name="addmenusuc"),
         path("mypagejumju",    views.MypageJumjuView.as_view(),    name="mypagejumju"),
         path("menulist",    views.MenuListView.as_view(),       name="menulist"),
         path( "addfav",        views.AddFavView.as_view(),         name="addfav"),             # Ȥ�� �� ���ã�� �߰��� url
         path("teststore",    views.TestStoreView.as_view(),    name="teststore"),
    ]
