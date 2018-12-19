# -*- coding: utf-8 -*-
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from cms.models.fields import PageField
from cms.models import CMSPlugin


class Icon(models.Model):
    name = models.CharField(max_length=32)
    icon = models.ImageField()


    def __str__(self):
        return self.name

class Blurb(CMSPlugin):
    icon = models.ForeignKey(Icon)
    headline = models.CharField(max_length=200)
    text = models.TextField(blank=True)
    link_text = models.CharField(max_length=40)
    link = PageField()
    def __str__(self):
        return self.headline
