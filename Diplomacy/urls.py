from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'Game.views.get_home', name='home'),
    url(r'^archives/$', 'Game.views.get_archives', name='archives'),
    url(r'^archives/((?P<id>[0-9]+))/$', 'Game.views.get_archive_detail', name='archive detail'),
    url(r'^players/$', 'Game.views.get_players', name='players'),
    url(r'^admin/', include(admin.site.urls)),
)
