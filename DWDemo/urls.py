"""DWDemo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views
from news.views import CategoryListView, CategoryDetailView
from django.contrib.auth.decorators import login_required
from news import views

admin.autodiscover()

urlpatterns = [
    url(r'^$', auth_views.login, {"template_name": "registration/login.html", 'redirect_authenticated_user': True}, name = 'login'),
    url(r'^category/$', login_required(CategoryListView.as_view()), name='list'),
    url(r'^category/(?P<pk>\d+)/$', login_required(CategoryDetailView.as_view()), name='Detail'),
    url(r'^news/', include('news.urls')),
    url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),
    url(r'^admin/', admin.site.urls),
    url(r'^signup/$', views.signup, name='signup'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

