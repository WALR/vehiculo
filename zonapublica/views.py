from django.shortcuts import render, render_to_response
from django.views.generic import TemplateView

# Create your views here.


# def index(request):
#     return render_to_response('zonapublica/index.html')

class index(TemplateView):
    template_name = 'zonapublica/index.html'