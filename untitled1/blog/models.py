# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models

from django.utils.encoding import python_2_unicode_compatible


# Create


@python_2_unicode_compatible
class Category(models.Model):
    name = models.CharField(u'名称', max_length=20)

    def __str__(self):
        return self.name;


@python_2_unicode_compatible
class Tag(models.Model):
    name = models.CharField(u'名称', max_length=20)

    def __str__(self):
        return self.name;


@python_2_unicode_compatible
class Article(models.Model):
    title = models.CharField(u'标题', max_length=150)

    body = models.TextField(u'正文')

    date = models.DateTimeField(u'发布时间')

    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name=u'分类')

    tags = models.ManyToManyField(Tag, verbose_name=u'标签', blank=True)

    # mo

    def __str__(self):
        return self.title

