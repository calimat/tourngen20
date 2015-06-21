from django.conf.urls import patterns, include, url
from django.contrib import admin

from tournaments import views

urlpatterns = [
    url(r'^$', views.home_page, name='home'),
    url(r'^tournaments/new$', views.new_tournament, name='new_list'),
    url(r'^tournaments/(\d+)/$', views.view_tournament, name='view_list'),
    url(r'^tournaments/(\d+)/add_team$', views.add_team, name='add_item'),
    # url(r'^admin/', include(admin.site.urls)),
]