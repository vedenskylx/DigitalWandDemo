# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField

class Category(models.Model):
    title = models.TextField(max_length=255)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return "/category/%i/" % self.id

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

class Article(models.Model):
    author = models.OneToOneField(User,
                                  verbose_name='Автор новости')
    category = models.OneToOneField(Category,
                                    verbose_name='Категория новости')
    title = models.TextField(max_length=255,
                             verbose_name='Заголовок')
    img = models.ImageField(upload_to='news',
                            height_field=100,
                            width_field=100,
                            blank=True,
                            null=True,
                            verbose_name='Изображение')
    content = HTMLField(max_length=10000,
                        verbose_name='Контент')
    datetime = models.DateTimeField(u'Дата публикации')

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return "/news/%i/" % self.id
    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

