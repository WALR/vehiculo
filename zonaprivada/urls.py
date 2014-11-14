from django.conf.urls import patterns, include, url
from .views import *

urlpatterns = patterns('',
    url(r'^zonaprivada/$', zonaprivada.as_view(), name='zonaprivada'),
)