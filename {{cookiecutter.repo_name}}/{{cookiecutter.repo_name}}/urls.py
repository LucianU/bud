from django.conf.urls import include, url


urlpatterns = [
    url(r'^$', '{{ cookiecutter.repo_name }}.views.under_construction',
        name='under_construction'),
]
