from django.conf.urls import patterns, url

from betterbirth import views

urlpatterns = patterns('',
    url(r'^$', views.makecsv, name='makecsv'),
)