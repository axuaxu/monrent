# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin

from .models import Monrent,Plinks

# Register your models here.

class PlinksAdmin(admin.ModelAdmin):
    fields = ['link']

class MonrentAdmin(admin.ModelAdmin):
    fields = ['title','address']

admin.site.register(Plinks,PlinksAdmin)
admin.site.register(Monrent,MonrentAdmin)


