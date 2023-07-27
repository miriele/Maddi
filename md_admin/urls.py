from django.urls.conf import path
from md_admin import views

app_name = "md_admin"

urlpatterns = [
    path("userlist",        views.UserlistView.as_view(),       name = "userlist"),     # ȸ�����
    path("userinfo",        views.UserinfoView.as_view(),       name = "userinfo"),     # ȸ����
    path("reviewlist",      views.ReviewlistView.as_view(),     name = "reviewlist"),   # ������
    path("reviewinfo",      views.ReviewinfoView.as_view(),     name = "reviewinfo"),   # �����
    path("sregistlist",     views.SregistlistView.as_view(),    name = "sregistlist"),  # ���ֵ�ϸ��
    path("sregistinfo",     views.SregistinfoView.as_view(),    name = "sregistinfo"),  # ���ֵ�ϻ�
    path("genstatis",       views.GenstatisView.as_view(),      name = "genstatis"),    # ȸ����� - ���� 
    path("agestatis",       views.AgestatisView.as_view(),      name = "agestatis"),    # ȸ����� - ����
    path("interestatis",    views.IntereView.as_view(),         name = "Interestatis"), # ȸ����� - ���ɻ� 
    path("tastestatis",     views.TasteView.as_view(),          name = "tastestatis"),  # ȸ����� - �Ը� 
    path("storestatis",     views.StoreView.as_view(),          name = "storestatis"),  # ��� - ������Ȳ
    path("dsrtstatis",      views.DsrtView.as_view(),           name = "dsrtstatis"),   # ȸ����� - ȸ������ ����Ʈ����
    path("drnkstatis",      views.DrnkView.as_view(),           name = "drnkstatis"),   # ȸ����� - ȸ������ ��������
    path("bdrnkstatis",     views.BdrnkView.as_view(),          name = "bdrnkstatis"),  # ȸ����� - �������� ��������
    path("bdsrtstatis",     views.BdsrtView.as_view(),          name = "bdsrtstatis"),  # ȸ����� - �������� ����Ʈ����
    path("iaostatis",       views.IaoView.as_view(),            name = "iaostatis"),    # ȸ����� - ����/��Ż 
    path("keystatis",       views.KeywordView.as_view(),        name = "keystatis"),    # ��� - �˻�Ű����
    ]