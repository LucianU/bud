from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin


urlpatterns = [
    url(settings.ADMIN_URL, include(admin.site.urls)),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^users/', include('users.urls', namespace='users')),
    url(r'^$', '{{ cookiecutter.project_name }}.views.under_construction',
        name='under_construction'),
]
