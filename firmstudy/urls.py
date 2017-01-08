"""firmstudy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf.urls import url,include
from django.contrib import admin
from studys import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^$',views.index,name='index'),
    url(r'^studys/article_list/$',views.article_list,name='article_list'),
    url(r'^(?P<article_id>\d+)/$',views.article_detail,name='article_detail'),
    url(r'^studys/method_list/$',views.method_list,name='method_list'),
    url(r'^(?P<article_id>\d+)/$',views.method_detail,name='method_detail'),
    url(r'^about$',views.about,name='about'),
]
