# -*- coding: utf-8 -*-
# RafKac
import datetime

from django.contrib import messages
from django.core.exceptions import ValidationError
from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.http import Http404
# from django.http import HttpResponse
from django.views import generic
from django.views.generic.edit import FormView

from stronaK.forms import ContactForm
from stronaK.models import News, Song, OldKnight


class IndexView(generic.ListView):
    template_name = 'stronaK/index.html'
    context_object_name = 'last_news'
    model = News
    queryset = News.objects.all()

    # def get_queryset(self):
    #     """Zwraca najnowsze aktualności"""
    #
    #     return get_list_or_404(News)
    #
    # def post(self, request):
    #     return render(request, self.template_name)


class ListOfSongView(generic.ListView):
    template_name = "stronaK/spiewnik.html"
    context_object_name = 'list_of_song'
    model = Song

    def get_queryset(self):
        """Zwraca wszystkie piosenki"""
        return get_list_or_404(Song)

    def post(self, request):
        """dodawanie, edycja, usuwanie lub wyszukiwanie piosenek"""
        if request.method == "POST":
            print("ListOfSongView - post")
            if request.POST.get('operation') == "delete":
                id = request.POST.get('id')
                print("usuniecie piosenki o ID: {}".format(id))
                deleted = get_object_or_404(Song, pk=id)
                print("piosenka do usunięcia: id: {}, tytuł: {}".format(id, deleted))
                # deleted.delete()

            if request.POST.get('operation') == "add":
                print("dodawanie piosenki ")
                return render(request, 'stronaK/dodawanie_piosenki.html')
            if request.POST.get('operation') == "edit":
                id = request.POST.get('id')
                print("edycja piosenki o ID: {}".format(id))
                return render(request, 'stronaK/edycja_piosenki.html')

        return render(request, self.template_name)


class ListOfOldView(generic.ListView):
    template_name = "stronaK/zmarli.html"
    context_object_name = 'list_of_old'
    model = OldKnight
    queryset = OldKnight.objects.all()

    # def get_queryset(self):
    #     """ Zwraca listę znanych starych Filistrów """
    #     return get_list_or_404(OldKnight)
    #
    # def post(self, request):
    #     return render(request, self.template_name)


class ContactFormView(FormView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = '/thanks/'

    def form_valid(self, form):
        # this method is called when valid data has been POSTed
        # it should return an HttpResponse
        form.send_email()
        return super().form_valid(form)


def response_story_of_Kujawja(request):
    return render(request, 'stronaK/historiaKujawji.html')


def response_story_of_corporations(request):
    return render(request, 'stronaK/historiaKorporacji.html')


def response_galeria(request):
    return render(request, 'stronaK/galeria.html')


def response_our_traditions(request):
    return render(request, 'stronaK/zwyczajeKujawickie.html')


def add_new_song(request):
    if request.method == 'POST':
        print('add_new_song - POST')
        print(datetime.datetime.now())

        try:
            title = request.POST.get('title')
            author = request.POST.get('author')
            text = request.POST.get('text')
            date = request.POST.get('date')
            comments = request.POST.get('comments')
            hidden = request.POST.get('hidden')

            new_song = Song(
                title=title,
                author=author,
                text=text,
                date=date,
                comments=comments,
                hidden=hidden
            )
            new_song.save()

        except ValueError:
            print('add_new_song - ValueError')
            messages.error(request, "dodawanie piosenek - ValueError")
        except ValidationError:
            print('add_new_song - ValidationError')
            messages.error(request, "dodawanie piosenek - ValidationError")
        else:
            messages.success(request, "dodawanie piosenek - sukces!")

        return render(request, 'stronaK/dodawanie_piosenki.html')

    print("dodawanie piosenki - GET: {}".format(datetime.datetime.now()))
    return render(request, 'stronaK/dodawanie_piosenki.html')


def edit_song(request):
    if request.method == 'POST':
        print('edit_song - POST')
        print(datetime.datetime.now())
        
        try:
            title = request.POST.get('title')
            author = request.POST.get('author')
            text = request.POST.get('text')
            date = request.POST.get('date')
            comments = request.POST.get('comments')
            hidden = request.POST.get('hidden')

            edited_song = Song(
                title=title,
                author=author,
                text=text,
                date=date,
                comments=comments,
                hidden=hidden,
            )
            edited_song.save()
   
        except ValueError:
            print('edit_song - ValueError')
            messages.error(request, "edycja piosenek - ValueError")
        except ValidationError:
            print('edit_song - ValidationError')
            messages.error(request, "edycja piosenek - ValidationError")
        else:
            messages.success(request, 'stronaK/edycja_piosenki.html')
    
    print('edycja piosenki - GET: {}'.format(datetime.datetime.now())) 
    return render(request, 'stronaK/edycja_piosenki.html')       


