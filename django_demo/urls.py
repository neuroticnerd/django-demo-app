""" django_demo URL Configuration """
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^', include('django_demo.main.urls', namespace='main')),
    url(
        r'^actions/',
        include('django_demo.actions.urls', namespace='actions')
    ),
    url(r'^admin/', include(admin.site.urls)),
]
