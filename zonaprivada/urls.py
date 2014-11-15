from django.conf.urls import patterns, include, url
from .views import *

urlpatterns = patterns('',
    url(r'^zonaprivada/$', zonaprivada.as_view(), name='zonaprivada'),
    url(r'^administador/$', zonaprivada.as_view(), name='zonaprivada'),
    url(r'^conductor/$', conductor.as_view(), name='conductor'),
    url(r'^conductor/viajes/$', conductor_viajes.as_view(), name='conductor_viajes'),
    url(r'^crear/$', crearcategoria.as_view(), name='crearcategoria'),
)