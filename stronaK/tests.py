# -*- coding: utf-8 -*-
# RafKac

from django.test import TestCase
from django.urls import reverse

from .models import News


class NewsModelTests(TestCase):
    def test_get_queryset(self):

        return 0

    def test_index(self):
        response = self.client.get(reverse('stronaK:index'))
        self.assertEqual(response.status_code, 200)


class OldKnightModelTests(TestCase):
    def test_get_queryset(self):
        return 0

    def test_(self):
        response = self.client.get(reverse('stronaK:zmarli.html'))
        self.assertEqual(response.status_code, 200)


class SongModelTests(TestCase):
    def test_get_queryset(self):
        return 0

    def test_(self):
        response = self.client.get(reverse('stronaK:spiewnik.html'))
        self.assertEqual(response.status_code, 200)
