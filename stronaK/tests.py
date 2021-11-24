# -*- coding: utf-8 -*-
# RafKac

from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from .models import News, OldKnight, Song


def create_news():
    return News.objects.create(
        date=timezone.now(),
        title="News dnia",
        text="Dolor amor sit omnia ",
        author_id='admin',
        comments="w pośpiechu stworzony",
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


class NewsModelTests(TestCase):
    def test_index_get_queryset(self):
        create_news()
        response = self.client.get(reverse('stronaK:index'))
        print(response.status_code)
        print("test_index_get_queryset: {}".format(response))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "News dnia")

    def test_index(self):
        create_news()
        response = self.client.get(reverse('stronaK:index'))
        print(response.status_code)
        print("test_index: {}".format(response))
        self.assertEqual(response.status_code, 200)


class OldKnightModelTests(TestCase):
    def test_zmarli_get_queryset(self):
        create_old_knight()
        response = self.client.get('stronaK:zmarli')
        print(response.status_code)
        print("test_zmarli_get_queryset: {}".format(response))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Jakub")

    def test_zmarli(self):
        create_old_knight()
        response = self.client.get('stronaK:zmarli')
        print(response.status_code)
        print("test_zmarli: {}".format(response))
        self.assertEqual(response.status_code, 200)


class SongModelTests(TestCase):
    def test_spiewnik_get_queryset(self):
        create_song()
        response = self.client.get(reverse('stronaK:spiewnik'))
        print(response.status_code)
        print("test_spiewnik_get_queryset: {}".format(response))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "kadrowa")

    def test_spiewnik(self):
        create_song()
        response = self.client.get(reverse('stronaK:spiewnik'))
        print(response.status_code)
        print("test_spiewnik: {}".format(response))
        self.assertEqual(response.status_code, 200)
