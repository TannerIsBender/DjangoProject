from __future__ import unicode_literals

from django.db import models

# Create your models here.

class PageCounter(models.Model):
        page = models.URLField(default='defaultPage')
        counter = models.IntegerField(default=0)
