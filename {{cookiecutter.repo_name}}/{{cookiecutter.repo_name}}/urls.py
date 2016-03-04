from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin


urlpatterns = [
    url(settings.ADMIN_URL, include(admin.site.urls)),
    url(r'^$', '{{ cookiecutter.repo_name }}.views.under_construction',
        name='under_construction'),
]
