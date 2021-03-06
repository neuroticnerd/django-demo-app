from __future__ import absolute_import, unicode_literals

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.ActionListView.as_view(), name='list'),
    url(
        r'^create/$',
        views.ActionCreateView.as_view(),
        name='create'
    ),
    url(
        r'^(?P<pk>\d+)/$',
        views.ActionDetailView.as_view(),
        name='detail'
    ),
    url(
        r'^(?P<pk>\d+)/update/$',
        views.ActionUpdateView.as_view(),
        name='edit'
    ),
    url(
        r'^(?P<pk>\d+)/delete/$',
        views.ActionDeleteView.as_view(),
        name='delete'
    ),
    url(
        r'^assign/$',
        views.ActionAssignView.as_view(),
        name='assign'
    ),
    url(
        r'^(?P<pk>\d+)/assign/$',
        views.ActionAssignView.as_view(),
        name='assign_action'
    ),
]
