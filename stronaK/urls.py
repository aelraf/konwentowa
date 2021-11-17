# -*- coding: utf-8 -*-
# RafKac
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('historiaKorporacji', views.index, name='historiaKorporacji'),
    path('spiewnik', views.index, name='spiewnik'),
    path('historiaKujawji', views.index, name='historiaKujawji'),
    path('zmarli', views.index, name='zmarli'),
]
