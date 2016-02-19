from __future__ import absolute_import, unicode_literals

from django.views import generic

from django_demo.accounts.utils import AuthenticatedView


class LandingView(generic.TemplateView):
    template_name = 'main/landing.html'


class DashboardView(AuthenticatedView, generic.TemplateView):
    template_name = 'main/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super(DashboardView, self).get_context_data(**kwargs)
        return context
