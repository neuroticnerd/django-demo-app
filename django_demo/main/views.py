from __future__ import absolute_import, unicode_literals

from django.views import generic


class DashboardView(generic.TemplateView):
    template_name = 'dashboard.html'

    def get_context_data(self, **kwargs):
        context = super(DashboardView, self).get_context_data(**kwargs)
        return context
