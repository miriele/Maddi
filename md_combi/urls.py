from django.urls.conf import path
from md_combi import views

app_name = "md_combi"

urlpatterns = [
    path( "comblist",      views.CombListView.as_view(),       name="comblist"),
    ]