# -*- coding: utf-8 -*-
# RafKac

from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import Http404
# from django.http import HttpResponse
from django.views import generic

from stronaK.models import News, Song, OldKnight


class IndexView(generic.ListView):
    template_name = 'stronaK/index.html'
    context_object_name = 'last_news'
    model = News

    def get_queryset(self):
        """Zwraca najnowsze aktualności"""

        return get_list_or_404(News)


class ListOfSongView(generic.ListView):
    template_name = "stronaK/spiewnik.html"
    context_object_name = 'list_of_song'
    model = Song

    def get_queryset(self):
        """Zwraca wszystkie piosenki"""
        return get_list_or_404(Song)


class ListOfOldView(generic.ListView):
    template_name = 'stronaK/zmarli.html'
    context_object_name = 'list_of_old'
    model = OldKnight

    def get_queryset(self):
        """ Zwraca listę znanych starych Filistrów """
        return get_list_or_404(OldKnight)


class StoryOfUsView(generic.DetailView):
    template_name = 'stronaK/historiaKujawji.html'


class StoryOfCorporationsView(generic.DetailView):
    template_name = 'stronaK/historiaKorporacji.html'



