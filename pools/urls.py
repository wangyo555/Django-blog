# _*_ coding: utf-8 _*_
# 开发团队：人生如逆旅
# 开发人员：Bill
# 开发时间：2019/9/4 12:08
# 文件名称：urls
# 开发工具：PyCharm

from django.urls import path
from . import views

app_name = 'pools'
urlpatterns = [
    path('', views.index, name='index'),

    path('<int:question_id>/', views.detail, name='detail'),

    path('<int:question_id>/results/', views.results, name='results'),

    path('<int:question_id>/vote/', views.vote, name='vote'),
]