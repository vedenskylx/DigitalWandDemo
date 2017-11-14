# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from news.models import Article,Category
admin.site.register(Category, verbose_name='Автор новости')
admin.site.register(Article)
