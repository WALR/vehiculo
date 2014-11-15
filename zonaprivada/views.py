from django.shortcuts import render, render_to_response
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from braces.views import LoginRequiredMixin, PermissionRequiredMixin, GroupRequiredMixin, AnonymousRequiredMixin
from django import template
from django.contrib.auth.models import Group
from .forms import categoriaForm
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf


class zonaprivada(LoginRequiredMixin, GroupRequiredMixin, TemplateView):
    template_name = 'zonaprivada/privada.html'
    login_url = "/conductor/"
    redirect_field_name = "/administrador/"
    group_required = u"admin"


class administrador(LoginRequiredMixin, GroupRequiredMixin, TemplateView):
    template_name = 'zonaprivada/privada.html'
    login_url = "/login/"
    group_required = u"admin"

class conductor(LoginRequiredMixin, GroupRequiredMixin, TemplateView):
    template_name = 'zonaprivada/conductor.html'
    login_url = "/login/"
    group_required = u"conductor"

class conductor_viajes(LoginRequiredMixin, GroupRequiredMixin, TemplateView):
    template_name = 'zonaprivada/conductor_viajes.html'
    login_url = "/login/"
    group_required = u"conductor"


class crearcategoria(FormView):
    template_name = 'zonaprivada/crear_categoria.html'
    form_class = categoriaForm
    success_url = '/thanks/'


# def crearcategoria(request):
#     context = {"form" : form}
#     template = "zonaprivada/crear_categoria.html"
#     return render(request, template, context)
    #optional

    # template_name = 'zonaprivada/privada.html'
    # login_url = "/login/"
    # group_required = u"admin"
    #required
    # group_required = u"admin"

    # def check_membership(self, group):
    #     if user_is_group:
    #         return u"/zonaprivada/admin/"
    #     else:
    #         return u"/zonaprivada/conductor/"



    # def get_authenticated_redirect_url(self):
    #     # if request.user|has_group:"mygroup"
    #      if self.request.user.has_group('admin'):
    #          return u"/zonaprivada/admin/"
    #      return u"/zonaprivada/conductor/"

    # def check_membership(self, group):
    #     ...
    #     # Check some other system for group membership
    #     if user_in_group:
    #         return True
    #     else:
    #         return False


# class SomeView(AnonymousRequiredMixin, TemplateView):
#     """ Redirect based on user level """
#     def get_authenticated_redirect_url(self):
#         if self.request.user.is_superuser:
#             return u"/admin/"
#         return u"/somewhere/else/"
