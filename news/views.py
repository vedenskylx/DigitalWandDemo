# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render

from news.models import Category
from news.models import Article
from django.views.generic import ListView, DetailView

class CategoryListView(ListView):
    model = Category

class CategoryDetailView(DetailView):
    model = Category

class ArticleListView(ListView):
    model = Article

class ArticleDetailView(DetailView):
    model = Article