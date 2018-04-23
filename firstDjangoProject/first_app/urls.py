# -*- coding:utf-8 -*-

from django.conf.urls import url
from first_app import views

urlpatterns = [
    url(r'^hello/', views.first_hello),
    url(r'hellogirl/',views.girl_hello)
]