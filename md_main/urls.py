from django.urls.conf import path
from md_main import views
urlpatterns = [
     path("main",views.MainView.as_view(),name="main"),
     # path("search",views.SearchView.as_view(),name="search"),
     ]