# -*- coding: utf-8 -*-
# RafKac

from django.shortcuts import render, get_list_or_404
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

    def post(self, request):
        return render(request, self.template_name)


class ListOfSongView(generic.ListView):
    template_name = "stronaK/spiewnik.html"
    context_object_name = 'list_of_song'
    model = Song

    def get_queryset(self):
        """Zwraca wszystkie piosenki"""
        return get_list_or_404(Song)

    def post(self, request):
        """dodawanie, edycja, usuwanie lub wyszukiwanie piosenek"""

        return render(request, self.template_name)


class ListOfOldView(generic.ListView):
    template_name = "stronaK/zmarli.html"
    context_object_name = 'list_of_old'
    model = OldKnight

    def get_queryset(self):
        """ Zwraca listę znanych starych Filistrów """
        return get_list_or_404(OldKnight)

    def post(self, request):
        return render(request, self.template_name)


def response_story_of_Kujawja(request):
    return render(request, 'stronaK/historiaKujawji.html')


def response_story_of_corporations(request):
    return render(request, 'stronaK/historiaKorporacji.html')


def response_galeria(request):
    return render(request, 'stronaK/galeria.html')


def response_our_traditions(request):
    return render(request, 'stronaK/zwyczajeKujawickie.html')



