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

    def get_queryset(self):
        """Zwraca najnowsze aktualności"""
        return News.objects.order_by('date')


def index(request):
    """
    główna strona - menu + aktualności + lista przycisków z lewej strony, przewijana wraz ze stroną
    """
    last_news = get_list_or_404(News)

    context = {'last_news': last_news}
    return render(request, 'stronaK/index.html', context)


class ListOfSongView(generic.ListView):
    template_name = "stronaK/spiewnik.html"
    context_object_name = 'list_of_song'

    def get_queryset(self):
        """Zwraca wszystkie piosenki"""
        return Song.objects.order_by('title')


def list_of_song(request):
    """
    czytamy z bazy piosenki i wyświetlamy po jednej na stronę,
    z przyciskami nawigacji na dole,
    zalogowany użytkownik ma możliwość edycji piosenki
    """

    return render(request, 'stronaK/spiewnik.html')


class ListOfOldView(generic.ListView):
    template_name = 'stronaK/zmarli.html'
    context_object_name = 'list_of_old'

    def get_queryset(self):
        """ Zwraca listę znanych starych Filistrów """
        return OldKnight.objects.order_by("surname")


def list_of_old(request):
    """
    czytamy z bazy listę zmarłych Kujawitów, wyświetlamy ich w tabeli po x,
    zalogowany użytkownik ma możliwość edytowania wpisów
    """

    context = {}
    return render(request, 'stronaK/zmarli.html', context)


class StoryOfUsView(generic.DetailView):
    template_name = 'stronaK/historiaKujawji.html'


def story_of_us(request):
    """
    Historia Kujawji wpisana na sztywno w HTMLa.
    """
    return render(request, 'stronaK/historiaKujawji.html')


class StoryOfCorporationsView(generic.DetailView):
    template_name = 'stronaK/historiaKorporacji.html'


def story_of_corporations(request):
    """
    Historia Polskich Korporacji Akademickich, sztywny tekst w HTML.
    """
    return render(request, 'stronaK/historiaKorporacji.html')


