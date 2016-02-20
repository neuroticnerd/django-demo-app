from __future__ import absolute_import, unicode_literals
from datetime import datetime

from django.contrib import messages
from django.contrib.auth.views import redirect_to_login
from django.utils.http import is_safe_url
from django.views import generic

from django_demo.accounts.utils import AuthenticatedView
from django_demo.actions.models import Action, ActionAssignment


class LandingView(generic.TemplateView):
    template_name = 'main/landing.html'


class DashboardView(AuthenticatedView, generic.TemplateView):
    template_name = 'main/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super(DashboardView, self).get_context_data(**kwargs)
        current_month = datetime.now().month
        assignments = ActionAssignment.objects.filter(
            created_at__month=current_month,
            action__created_at__month=current_month,
            user=self.request.user
        ).select_related('action')
        context['assigned_actions'] = [a.action for a in assignments]
        context['month_actions'] = Action.objects.filter(
            created_at__month=current_month
        )
        context['created_actions'] = Action.objects.filter(
            created_by=self.request.user
        )
        return context


class DebugView(AuthenticatedView, generic.TemplateView):
    template_name = 'main/debug.html'

    def dispatch(self, *args, **kwargs):
        if not self.request.user.is_superuser:
            msg = (
                'You must be authenticated as a superuser '
                'user to access the requested page.'
            )
            messages.error(self.request, msg)
            redirect_to = self.request.META.get('HTTP_REFERER', '/')
            if not is_safe_url(url=redirect_to, host=self.request.get_host()):
                redirect_to = '/'
            return redirect_to_login(redirect_to)
        return super(DebugView, self).dispatch(*args, **kwargs)
