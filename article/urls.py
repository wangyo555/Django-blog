# _*_ coding: utf-8 _*_
# 开发团队：人生如逆旅
# 开发人员：Bill
# 开发时间：2019/9/10 15:45
# 文件名称：urls
# 开发工具：PyCharm

from django.urls import path
from . import views

urlpatterns = [
    path('', views.article_list, name='article_list'),
    path('<int:article_id>', views.article_detail, name='article_detail')

]