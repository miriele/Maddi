from django.urls.conf import path
from md_combi import views

app_name = "md_combi"

urlpatterns = [
    path( "comblist",      views.CombListView.as_view(),        name="comblist"),   # 추천 글목록 보기
    path( "combwrite",     views.CombWriteView.as_view(),       name="combwrite"),  # 추천글 작성하기
    path( "combd",         views.CombDView.as_view(),           name="combd"),      # 추천글 내용 보기
    path( "clike",        views.CLikeView.as_view(),          name="clike"),      # 좋아요 
    ]