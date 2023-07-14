from django.urls.conf import path
from md_store import views

app_name = "md_store"

urlpatterns = [
         path( "info", views.InfoView.as_view(), name="info" ),
       
       ]