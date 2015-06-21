from django.conf.urls import patterns, include, url
from django.contrib import admin

from tournaments import views
from django.conf.urls import url

urlpatterns = [
    url(r'^new$', views.new_tournament, name='new_tournament'),
    url(r'^(\d+)/$', views.view_tournament, name='view_tournament'),
    url(r'^(\d+)/add_team$', views.add_team, name='add_team'),
]
