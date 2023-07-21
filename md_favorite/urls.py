from django.urls.conf import path
from md_favorite import views

app_name = "md_favorite"

urlpatterns = [
    path( "favorite",      views.FavoriteView.as_view(),       name="favorite"),      #즐겨찾기 목록 보기
    path( "addfav",        views.AddFavView.as_view(),         name="addfav"),             # 혹시 모를 즐겨찾기 추가용 url
    ]