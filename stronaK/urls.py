# -*- coding: utf-8 -*-
# RafKac
from django.urls import path
from . import views

app_name = 'stronaK'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('historiaKorporacji', views.StoryOfCorporationsView.as_view(), name='historiaKorporacji'),
    path('spiewnik', views.ListOfSongView.as_view(), name='spiewnik'),
    path('historiaKujawji', views.StoryOfUsView.as_view(), name='historiaKujawji'),
    path('zmarli', views.ListOfOldView.as_view(), name='zmarli'),
]
