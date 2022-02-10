# -*- coding: utf-8 -*-
# RafKac
from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from .models import News, OldKnight, Song


def create_news():
    return News.objects.create(
        date=timezone.now(),
        title="News dnia",
        text="Dolor amor sit omnia ",
        author_id=User.objects.create(id=1, username="Macias"),
        hidden=False,
        picture=None
    )


def create_old_knight():
    return OldKnight.objects.create(
        name="Jakub",
        last_name="Wędrowycz",
        date_birth=None,
        date_death=None,
        comments="nieznany czas życia",
    )


def create_song():
    return Song.objects.create(
        title='Pierwsza kadrowa',
        text="Raduje się serce, raduje się dusza, gdy pierwsza kadrowa...",
        author="Nieznany",
        date=None,
        comments="piosenka wojskowa, skoczna melodia",
        hidden=False
    )


def create_song_from_data(title, text, author, date=None, comments=None, hidden=False):
    return Song.objects.create(
        title=title,
        text=text,
        author=author,
        date=date,
        comments=comments,
        hidden=hidden
    )


class NewsModelTests(TestCase):
    def setUp(self) -> None:
        create_news()

    def test_index_get_queryset(self):
        response = self.client.get(reverse('stronaK:index'))
        self.assertEqual(response.status_code, 200)

        last_news = News.objects.all()
        self.assertQuerysetEqual(response.context['last_news'], last_news)

    def test_index(self):
        response = self.client.get(reverse('stronaK:index'))
        self.assertEqual(response.status_code, 200)

    def test_index_no_news(self):
        response = self.client.get(reverse('stronaK:index'))
        self.assertEqual(response.status_code, 200)


class OldKnightModelTests(TestCase):
    def setUp(self) -> None:
        create_old_knight()

    def test_zmarli_get_queryset(self):
        response = self.client.get(reverse('stronaK:zmarli'))
        self.assertEqual(response.status_code, 200)

        list_of_old = OldKnight.objects.all()
        self.assertQuerysetEqual(response.context['list_of_old'], list_of_old)

    def test_zmarli(self):
        response = self.client.get(reverse('stronaK:zmarli'))

        self.assertEqual(response.status_code, 200)


class SongModelTests(TestCase):
    def setUp(self) -> None:
        create_song()
        create_song_from_data("Druga piosenka", "dzien dobry, przyjaciele, dzisiaj...", "Jan Kasprowicz")

    def test_spiewnik_get_queryset(self):
        response = self.client.get(reverse('stronaK:spiewnik'))
        self.assertEqual(response.status_code, 200)

        list_of_song = Song.objects.all()
        self.assertQuerysetEqual(response.context['list_of_song'], list_of_song)

    def test_spiewnik(self):
        response = self.client.get(reverse('stronaK:spiewnik'))
        self.assertEqual(response.status_code, 200)

    def test_spiewnik_post(self):
        songs = Song.objects.all()
        response = self.client.post(reverse('stronaK:spiewnik'), {'operation': 'delete', 'id': 1})
        self.assertEqual(response.status_code, 200)

        song_after_delete = Song.objects.all().count()

        self.assertEqual(song_after_delete, songs.count())

        response = self.client.post(reverse('stronaK:spiewnik'), {'operation': 'edit', 'id': 2})
        self.assertEqual(response.status_code, 200)

        response = self.client.post(reverse('stronaK:spiewnik'), {'operation': 'add'})
        self.assertEqual(response.status_code, 200)


class ClassicalViewsTests(TestCase):
    def test_response_story_of_Kujawja(self):
        response = self.client.get(reverse('stronaK:historiaKujawji'))
        self.assertEqual(response.status_code, 200)

    def test_response_story_of_corporations(self):
        response = self.client.get(reverse('stronaK:historiaKorporacji'))
        self.assertEqual(response.status_code, 200)

    def test_response_galeria(self):
        response = self.client.get(reverse('stronaK:galeria'))
        self.assertEqual(response.status_code, 200)

    def test_response_our_traditions(self):
        response = self.client.get(reverse('stronaK:zwyczajeKujawickie'))
        self.assertEqual(response.status_code, 200)
