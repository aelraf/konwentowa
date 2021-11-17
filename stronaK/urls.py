# -*- coding: utf-8 -*-
# RafKac
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
]
