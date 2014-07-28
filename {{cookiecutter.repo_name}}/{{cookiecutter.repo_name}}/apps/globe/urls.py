from django.conf.urls import patterns, url


urlpatterns = patterns('',
    url(r'^$', 'globe.views.under_construction', name='under_construction'),
)
