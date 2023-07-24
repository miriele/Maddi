from django.urls.conf import path
from md_member import views

app_name = "md_member"

urlpatterns = [
    path( "login",       views.LoginView.as_view(),       name="login"),
    path( "logout",      views.LogoutView.as_view(),      name="logout"),
    path( "input",       views.InputView.as_view(),       name="input" ),
    path( "idcheck",     views.IdCheckView.as_view(),     name="idcheck" ),
    path( "nickcheck",   views.NickCheckView.as_view(),   name="nickcheck" ),
    path( "userinfo",    views.UserInfoView.as_view(),    name="userinfo"),
    path( "myorderlist",    views.MyOrderListView.as_view(),    name="myorderlist"),
    ]