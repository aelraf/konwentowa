# -*- coding: utf-8 -*-
# RafKac
from django.contrib import admin

from .models import News, Song, OldKnight


# udostępniamy News, Song i OldKnights do modyfikacji w panelu administracyjnym
admin.site.register(News)
admin.site.register(Song)
admin.site.register(OldKnight)

