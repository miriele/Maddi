from django.urls.conf import path
from md_favorite import views

app_name = "md_favorite"

urlpatterns = [
    path( "favorite",      views.FavoriteView.as_view(),       name="favorite"),      #즐겨찾기 목록 보기
    ]