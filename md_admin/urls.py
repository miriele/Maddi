from django.urls.conf import path
from md_admin import views

app_name = "md_admin"

urlpatterns = [
    path("userlist",  views.UserlistView.as_view(), name="userlist"),
    path("userinfo",  views.UserinfoView.as_view(), name="userinfo"),
    path("reviewlist",  views.ReviewlistView.as_view(), name="reviewlist"),
    path("reviewinfo",  views.ReviewinfoView.as_view(), name="reviewinfo"),
    path("sregistlist",  views.SregistlistView.as_view(), name="sregistlist"),
    path("sregistinfo",  views.SregistinfoView.as_view(), name="sregistinfo"),
    ]