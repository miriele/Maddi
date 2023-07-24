from django.urls.conf import path
from md_main import views
urlpatterns = [
     path("main",       views.MainView.as_view(),   name="main"),
     path("searchlist", views.SearchView.as_view(), name="searchlist"),
     path("map", views.MapView.as_view(), name="map"),
     ]