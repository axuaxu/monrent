from __future__ import unicode_literals

from django.db import models

# Create your models here.

class plinks(models.Model):
    link = models.CharField(max_length=200)


