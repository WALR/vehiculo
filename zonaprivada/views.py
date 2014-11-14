from django.shortcuts import render
from django.views.generic import TemplateView
from braces.views import LoginRequiredMixin, PermissionRequiredMixin, GroupRequiredMixin, AnonymousRequiredMixin
from django import template
from django.contrib.auth.models import Group


class zonaprivada(LoginRequiredMixin, TemplateView):
    template_name = 'zonaprivada/privada.html'
    login_url = "/login/"



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
