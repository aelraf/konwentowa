# -*- coding: utf-8 -*-
# RafKac

from django.shortcuts import render
# from django.http import HttpResponse


def index(request):

    return render(request, 'stronaK/index.html')


def list_of_song(request):
    """
    czytamy z bazy piosenki i wyświetlamy po jednej na stronę,
    z przyciskami nawigacji na dole,
    zalogowany użytkownik ma możliwość edycji piosenki
    """

    return render(request, 'stronaK/spiewnik.html')


def list_of_old(request):
    """
    czytamy z bazy listę zmarłych Kujawitów, wyświetlamy ich w tabeli po x,
    zalogowany użytkownik ma możliwość edytowania wpisów
    """

    context = {}
    return render(request, 'stronaK/zmarli.html', context)


def story_of_us(request):
    """
    Historia Kujawji wpisana na sztywno w HTMLa.
    """
    return render(request, 'stronaK/historiaKujawji.html')


def story_of_corporations(request):
    """
    Historia Polskich Korporacji Akademickich, sztywny tekst w HTML.
    """
    return render(request, 'stronaK/historiaKorporacji.html')


