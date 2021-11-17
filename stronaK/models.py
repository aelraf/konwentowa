# -*- coding: utf-8 -*-
# RafKac
from django.conf import settings
from django.db import models


class OldKnight(models.Model):
    name = models.TextField(null=True)
    last_name = models.TextField(null=False)
    date_birth = models.IntegerField(null=True)
    date_death = models.IntegerField(null=True)
    comments = models.TextField(null=True)


class Song(models.Model):
    title = models.TextField(null=False)
    text = models.TextField(null=False)
    author = models.TextField(null=True)
    date = models.TextField(null=True)
    comments = models.TextField(null=True)
    hidden = models.BooleanField(null=False, default=True)


class News(models.Model):
    title = models.TextField(null=False)
    text = models.TextField(null=False)
    date = models.DateField(null=False)
    author_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)
    picture = models.ImageField(null=True)
    hidden = models.BooleanField(null=False, default=True)
