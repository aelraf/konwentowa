# -*- coding: utf-8 -*-
# RafKac
from django.urls import path
from . import views

app_name = 'stronaK'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('historiaKorporacji', views.response_story_of_corporations, name='historiaKorporacji'),
    path('spiewnik', views.ListOfSongView.as_view(), name='spiewnik'),
    path('historiaKujawji', views.response_story_of_Kujawja, name='historiaKujawji'),
    path('zmarli', views.ListOfOldView.as_view(), name='zmarli'),
    path('zwyczajeKujawickie', views.response_our_traditions, name="zwyczajeKujawickie"),
    path('galeria', views.response_galeria, name="galeria"),
]
