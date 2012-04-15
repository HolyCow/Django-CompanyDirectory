from django.conf.urls import patterns, include, url

urlpatterns = patterns('companydirectory.views',
    url(r'^$', 'index'),
)

