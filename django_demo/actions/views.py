from __future__ import absolute_import, unicode_literals

import logging

from django.contrib import messages
from django.contrib.auth.views import redirect_to_login
from django.core.urlresolvers import reverse, reverse_lazy
from django.utils.http import is_safe_url
from django.views import generic

from django_demo.accounts.utils import AuthenticatedView
from django_demo.actions.models import Action


class ActionListView(AuthenticatedView, generic.ListView):
    model = Action

    def get_context_data(self, **kwargs):
        context = super(ActionListView, self).get_context_data(**kwargs)
        return context


class ActionDetailView(AuthenticatedView, generic.DetailView):
    model = Action


class ActionUpdateView(AuthenticatedView, generic.UpdateView):
    model = Action
    fields = ('title', 'description')

    def dispatch(self, *args, **kwargs):
        if not self.request.user.is_staff:
            msg = (
                'You must be authenticated as a staff '
                'user to perform that action.'
            )
            messages.error(self.request, msg)
            redirect_to = self.request.META.get('HTTP_REFERER', '/')
            if not is_safe_url(url=redirect_to, host=self.request.get_host()):
                redirect_to = '/'
            return redirect_to_login(redirect_to)
        return super(ActionUpdateView, self).dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        log = logging.getLogger(__name__)
        context = super(ActionUpdateView, self).get_context_data(**kwargs)
        cancel_url = self.request.META.get('HTTP_REFERER')
        log.debug(cancel_url)
        if cancel_url is not None:
            if is_safe_url(url=cancel_url, host=self.request.get_host()):
                context['cancel_url'] = cancel_url
        return context

    def get_success_url(self):
        return reverse('actions:detail', kwargs={'pk': self.object.id})


class ActionDeleteView(AuthenticatedView, generic.DeleteView):
    model = Action
    success_url = reverse_lazy('actions:list')

    def dispatch(self, *args, **kwargs):
        if not self.request.user.is_staff:
            msg = (
                'You must be authenticated as a staff '
                'user to perform that action.'
            )
            messages.error(self.request, msg)
            redirect_to = self.request.META.get('HTTP_REFERER', '/')
            if not is_safe_url(url=redirect_to, host=self.request.get_host()):
                redirect_to = '/'
            return redirect_to_login(redirect_to)
        return super(ActionDeleteView, self).dispatch(*args, **kwargs)
