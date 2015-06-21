from django.conf.urls import include, url
from tournaments import views as list_views  #1
from tournaments import urls as list_urls  #2

urlpatterns = [
    url(r'^$', list_views.home_page, name='home'),
    url(r'^tournaments/', include(list_urls)),
    # url(r'^admin/', include(admin.site.urls)),
]