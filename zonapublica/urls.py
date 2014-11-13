from django.conf.urls import patterns, include, url
from .views import index, empresa, historial, convertidor, contacto


urlpatterns = patterns('',
    url(r'^$', index.as_view(), name='index'),
    url(r'^empresa/$', empresa.as_view(), name='empresa'),
    url(r'^historial/$', historial.as_view(), name='historial'),
    url(r'^convertidor/$', convertidor.as_view(), name='convertidor'),
    url(r'^contacto/$', contacto.as_view(), name='contacto'),
    url(r'^login/$' , 'django.contrib.auth.views.login',
        {'template_name':'login.html'}, name='login'),
    url(r'^cerrar/$' , 'django.contrib.auth.views.logout_then_login',
         name='logout'),
)