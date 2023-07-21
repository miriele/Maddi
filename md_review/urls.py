from django.urls.conf import path
from md_review import views

app_name = "md_review"

urlpatterns = [
    path( "revwrite",      views.RevwriteView .as_view(),       name="revwrite"),     # 리뷰 작성 폼
    path( "review",        views.ReviewView .as_view(),         name="review"),     # 리뷰 보기 폼>매뉴 정보페이지에 합체
    ]