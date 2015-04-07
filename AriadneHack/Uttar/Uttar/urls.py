from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Uttar.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^sms/$', 'betterbirth.views.sms'),

    url(r'^makecsv/$', include('betterbirth.urls')),
)

from django.conf.urls import patterns, include, url
