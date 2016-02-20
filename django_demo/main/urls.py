from __future__ import absolute_import, unicode_literals

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.LandingView.as_view(), name='landing'),
    url(r'^dashboard/$', views.DashboardView.as_view(), name='dashboard'),
    url(r'^debug/$', views.DebugView.as_view(), name='debug'),
]
