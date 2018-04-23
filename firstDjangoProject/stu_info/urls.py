# -*- coding:utf-8 -*-
from django.conf.urls import url
from stu_info import views

urlpatterns = [
    url(r'^welcome/', views.welcome),
    url(r'^addstudent/', views.addStudent),
]

