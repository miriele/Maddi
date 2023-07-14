from django.urls.conf import path
from md_member import views

app_name = "md_member"

urlpatterns = [
    # path("Aaaa",       views.AaaaView.as_view(),       name="Aaaa"),    # view 추가하면 삭제하세요
    path( "login",    views.LoginView.as_view(),       name="login"),
    path( "logout",   views.LogoutView.as_view(),      name="logout"),
    path( "input",    views.InputView.as_view(),       name="input" ),
  
    
    
    ]