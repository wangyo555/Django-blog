# _*_ coding: utf-8 _*_
# 开发团队：人生如逆旅
# 开发人员：Bill
# 开发时间：2019/8/30 23:33
# 文件名称：view
# 开发工具：PyCharm

from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    return HttpResponse('I love u')


