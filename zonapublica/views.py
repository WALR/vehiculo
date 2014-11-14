from django.shortcuts import render, render_to_response
from django.views.generic import TemplateView


class index(TemplateView):
    template_name = 'zonapublica/index.html'

class empresa(TemplateView):
    template_name = 'zonapublica/empresa.html'


class historial(TemplateView):
    template_name = 'zonapublica/historial.html'

class convertidor(TemplateView):
    template_name = 'zonapublica/convertidor.html'

class contacto(TemplateView):
    template_name = 'zonapublica/contacto.html'