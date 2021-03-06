# -*- coding: utf-8 -*-
# RafKac
from django.conf import settings
from django.db import models


class OldKnight(models.Model):
    name = models.TextField(null=True, blank=True)
    last_name = models.TextField(null=False)
    date_birth = models.DateField(null=True, blank=True)
    date_death = models.DateField(null=True, blank=True)
    comments = models.TextField(null=True, blank=True)

    class Meta:
        ordering = ['last_name']

    def __str__(self):
        return str(self.name) + " " + str(self.last_name)


class Song(models.Model):
    title = models.TextField(null=False)
    text = models.TextField(null=False)
    author = models.TextField(null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    comments = models.TextField(null=True, blank=True)
    hidden = models.BooleanField(null=False, default=True)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title


class News(models.Model):
    title = models.TextField(null=False)
    text = models.TextField(null=False)
    date = models.DateField(null=False, auto_now_add=True)
    author_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)
    picture = models.ImageField(null=True, blank=True)
    hidden = models.BooleanField(null=False, default=True)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return str(self.title) + " " + str(self.date) + " " + str(self.author_id)
