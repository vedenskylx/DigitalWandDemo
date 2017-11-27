# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from django import forms
from django.dispatch import receiver
from django.db.models.signals import post_save

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)

    username = 'demo'

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']

class Category(models.Model):
    title = models.TextField(max_length=255)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return "/category/%i/" % self.id

    def get_news(self):
        return Article.objects.filter(category=self)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

class Article(models.Model):
    author = models.ForeignKey(User,
                                  verbose_name='Автор новости')
    category = models.ForeignKey(Category,
                                    verbose_name='Категория новости')
    title = models.TextField(max_length=255,
                             verbose_name='Заголовок')
    img = models.ImageField(upload_to='media/uploads',
                            blank=True,
                            null=True,
                            verbose_name='Изображение')
    content = HTMLField(max_length=10000,
                        verbose_name='Контент')
    datetime = models.DateTimeField(u'Дата публикации')

    def __unicode__(self):
        return self.title

    def get_user_name(self):
        return User.objects.select_related().filter(id=self.author.id)[0]

    def get_absolute_url(self):
        return "/news/%i/" % self.id
    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

