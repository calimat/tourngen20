from django.conf.urls import patterns, include, url
from django.contrib import admin

from tournaments import views

urlpatterns = [
    url(r'^$', views.home_page, name='home'),
    url(r'^tournaments/the-only-tournament-in-the-world/$', views.view_tournament, name='view_tournament'),
    # url(r'^admin/', include(admin.site.urls)),
]
