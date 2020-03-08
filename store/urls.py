from django.urls import path,include,re_path
from django.conf.urls import url
from django.conf import settings
from django.contrib import admin
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^/(?P<album_id>[0-9]+)/$', views.detail),
    path('/search',views.search)
]