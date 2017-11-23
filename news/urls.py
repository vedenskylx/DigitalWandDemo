#coding: utf-8
from django.conf.urls import url, include

from news.views import ArticleDetailView

urlpatterns = [
    url(r'^(?P<pk>\d+)/$', ArticleDetailView.as_view(), name='detail'),
]