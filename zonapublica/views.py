from django.shortcuts import render, render_to_response
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

class LoginRequiredMixin(object):
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(LoginRequiredMixin, self).dispatch(request, *args, **kwargs)


 # @method_decorator(login_required)
 #    def dispatch(self, request, *args, **kwargs):
 #        if not request.user.has_perms(self.required_permissions):
 #            messages.error(
 #                request,
 #                'You do not have the permission required to perform the '
 #                'requested operation.')
 #            return redirect(settings.LOGIN_URL)
 #        return super(PermissionsRequiredMixin, self).dispatch(
 #            request, *args, **kwargs)

# class LoginRequiredMixin(object):
#     """
#     View mixin which requires that the user is authenticated.
#     """
#     @method_decorator(login_required)
#     def dispatch(self, request, *args, **kwargs):
#         return super(LoginRequiredMixin, self).dispatch(
#             self, request, *args, **kwargs)


class index(TemplateView):
    template_name = 'zonapublica/index.html'

class empresa(TemplateView):
    template_name = 'zonapublica/empresa.html'


class historial(TemplateView):
    template_name = 'zonapublica/historial.html'

class convertidor(LoginRequiredMixin, TemplateView):
    template_name = 'zonapublica/convertidor.html'

class contacto(TemplateView):
    template_name = 'zonapublica/contacto.html'