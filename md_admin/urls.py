from django.urls.conf import path
from md_admin import views

app_name = "md_admin"

urlpatterns = [
    path("userlist",        views.UserlistView.as_view(),       name = "userlist"),
    path("userinfo",        views.UserinfoView.as_view(),       name = "userinfo"),
    path("reviewlist",      views.ReviewlistView.as_view(),     name = "reviewlist"),
    path("reviewinfo",      views.ReviewinfoView.as_view(),     name = "reviewinfo"),
    path("sregistlist",     views.SregistlistView.as_view(),    name = "sregistlist"),
    path("sregistinfo",     views.SregistinfoView.as_view(),    name = "sregistinfo"),
    path("genstatis",       views.GenstatisView.as_view(),      name = "genstatis"),
    path("agestatis",       views.AgestatisView.as_view(),      name = "agestatis"),
    path("interestatis",    views.IntereView.as_view(),         name = "Interestatis"),
    path("tastestatis",     views.TasteView.as_view(),          name = "tastestatis"),
    path("storestatis",     views.StoreView.as_view(),          name = "storestatis"),
    path("dsrtstatis",      views.DsrtView.as_view(),           name = "dsrtstatis"),
    path("drnkstatis",      views.DrnkView.as_view(),           name = "drnkstatis"),
    path("bdrnkstatis",     views.BdrnkView.as_view(),          name = "bdrnkstatis"),
    path("bdsrtstatis",     views.BdsrtView.as_view(),          name = "bdsrtstatis"),
    ]