# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin

from .models import Monrent,Plinks

# Register your models here.

class PlinksAdmin(admin.ModelAdmin):
    fields = ['link']

class MonrentAdmin(admin.ModelAdmin):
    #fields = ['title','address']
    list_display = ('num','udate','title','address','pcode','rent','rooms','rstyle','intime','method','length')

class MonrentProxy(Monrent):
    class Meta:
        proxy = True
class MonrentProxyAdmin(admin.ModelAdmin):
    list_display = ('num','udate','title','pcode','rooms','rent') 
    list_filter = ('pcode','rooms')
admin.site.register(Plinks,PlinksAdmin)
admin.site.register(Monrent,MonrentAdmin)
admin.site.register(MonrentProxy,MonrentProxyAdmin)

