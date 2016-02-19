from __future__ import absolute_import, unicode_literals
from datetime import datetime

from django.views import generic

from django_demo.accounts.utils import AuthenticatedView
from django_demo.actions.models import Action


class LandingView(generic.TemplateView):
    template_name = 'main/landing.html'


class DashboardView(AuthenticatedView, generic.TemplateView):
    template_name = 'main/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super(DashboardView, self).get_context_data(**kwargs)
        current_month = datetime.now().month
        context['month_actions'] = Action.objects.filter(
            created_at__month=current_month
        )
        context['my_actions'] = Action.objects.filter(
            created_at__month=current_month,
            created_by=self.request.user
        )
        return context
