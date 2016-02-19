from __future__ import absolute_import, unicode_literals

from django.conf.urls import url

from . import views

urlpatterns = (
    url(r'^login/$', views.LoginView.as_view(), name='login'),
    url(r'^logout/$', views.LogoutView.as_view(), name='logout'),
    url(r'^profile/$', views.ProfileView.as_view(), name='profile'),
)
