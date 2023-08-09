from django.urls.conf import path
from md_admin import views
from .views import search

app_name = "md_admin"

urlpatterns = [
    path("userlist",        views.UserlistView.as_view(),       name = "userlist"),     # 회원목록
    path("userinfo",        views.UserinfoView.as_view(),       name = "userinfo"),     # 회원상세
    path("reviewlist",      views.ReviewlistView.as_view(),     name = "reviewlist"),   # 리뷰목록
    path("reviewinfo",      views.ReviewinfoView.as_view(),     name = "reviewinfo"),   # 리뷰상세
    path("sregistlist",     views.SregistlistView.as_view(),    name = "sregistlist"),  # 점주등록목록
    path("sregistinfo",     views.SregistinfoView.as_view(),    name = "sregistinfo"),  # 점주등록상세
    path("genstatis",       views.GenstatisView.as_view(),      name = "genstatis"),    # 회원통계 - 성별 
    path("agestatis",       views.AgestatisView.as_view(),      name = "agestatis"),    # 회원통계 - 연령
    path("interestatis",    views.IntereView.as_view(),         name = "Interestatis"), # 회원통계 - 관심사 
    path("tastestatis",     views.TasteView.as_view(),          name = "tastestatis"),  # 회원통계 - 입맛 
    path("storestatis",     views.StoreView.as_view(),          name = "storestatis"),  # 통계 - 매장현황
    path("dsrtstatis",      views.DsrtView.as_view(),           name = "dsrtstatis"),   # 회원통계 - 회원정보 디저트취향
    path("drnkstatis",      views.DrnkView.as_view(),           name = "drnkstatis"),   # 회원통계 - 회원정보 음료취향
    path("bdrnkstatis",     views.BdrnkView.as_view(),          name = "bdrnkstatis"),  # 회원통계 - 구매정보 음료취향
    path("bdsrtstatis",     views.BdsrtView.as_view(),          name = "bdsrtstatis"),  # 회원통계 - 구매정보 디저트취향
    path("iaostatis",       views.IaoView.as_view(),            name = "iaostatis"),    # 회원통계 - 유입/이탈 
    path("keystatis",       views.KeywordView.as_view(),        name = "keystatis"),    # 통계 - 검색키워드
    path('searched',        views.search,                       name = 'search'),
    path("testorder",       views.TestOrderView.as_view(),      name = "testorder"),    # 점주 주문 확인 처럼 테스트 확인용
    path("tordr",           views.TOrdrView.as_view(),          name = "tordr"),        # test ajax (폼없이)
    ]