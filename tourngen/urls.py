from django.conf.urls import patterns, include, url
from django.contrib import admin

from tournaments import views

urlpatterns = [
    url(r'^$', views.home_page, name='home'),
    url(r'^tournaments/new$', 'tournaments.views.new_tournament', name='new_tournament'),
    url(r'^tournaments/(.+)/$', 'tournaments.views.view_tournament', name='view_tournament'),
    # url(r'^admin/', include(admin.site.urls)),
]
