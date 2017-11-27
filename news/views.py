# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.conf import settings
from news.models import Category
from news.models import Article
from django.views.generic import ListView, DetailView

from django.http import HttpResponseRedirect

from django.shortcuts import render, redirect
from .forms import SignupForm

class CategoryListView(ListView):
    model = Category

class CategoryDetailView(DetailView):
    model = Category

class ArticleListView(ListView):
    model = Article

class ArticleDetailView(DetailView):
    model = Article

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            redirect_to = settings.LOGIN_URL
            user = form.save(commit=False)
            user.is_active = True
            user.username = user.email
            user.save()

            return HttpResponseRedirect(redirect_to)
    else:
        form = SignupForm()
    return render(request, 'registration/signup.html', {
        'form': form,
    })