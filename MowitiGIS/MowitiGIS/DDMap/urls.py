from django.conf.urls import url
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import HomePageView, poi_datasets, canale_datasets, asezari_datasets, pensiune_datasets, \
    arbori_datasets, localitate_datasets, pescuit_datasets, colonie_datasets, apascazuta_datasets, vegetatie_datasets, \
    punctlansare_datasets, camping_datasets, colmatat_datasets, grind_datasets, padure_datasets, ariiprotejate_datasets, \
    LineChartJSONView, afisare_ture, rute_tura, create_poi

urlpatterns =[

    url(r'^$', HomePageView.as_view(), name='home'),
    url(r'^DDGraph/$', LineChartJSONView.as_view(), name='grafic'),
    url(r'^poi_data/$', poi_datasets, name='poi_page'),
    url(r'^asezari_data/$', asezari_datasets, name='asezari_page'),
    url(r'^pensiuni_data/$', pensiune_datasets, name='pensiune_page'),
    url(r'^arbori_data/$', arbori_datasets, name='arbori_page'),
    url(r'^localitate_data/$', localitate_datasets, name='localitate_page'),
    url(r'^pescuit_data/$', pescuit_datasets, name='pescuit_page'),
    url(r'^colonie_data/$', colonie_datasets, name='colonie_page'),
    url(r'^apascazuta_data/$', apascazuta_datasets, name='apascazuta_page'),
    url(r'^vegetatie_data/$', vegetatie_datasets, name='vegetatie_page'),
    url(r'^punctlansare_data/$', punctlansare_datasets, name='punctlansare_page'),
    url(r'^camping_data/$', camping_datasets, name='camping_page'),
    url(r'^colmatat_data/$', colmatat_datasets, name='colmatat_page'),
    url(r'^grinduri_data/$', grind_datasets, name='grind_page'),
    url(r'^paduri_data/$', padure_datasets, name='paduri_page'),
    url(r'^ariiprotejate_data/$', ariiprotejate_datasets, name='ariiprotejate_page'),
    url(r'^canale/$', canale_datasets, name='canale_page'),
    url(r'^ture/$', afisare_ture, name='ture_page'),
    path('rute_tura/<int:id_tura>', rute_tura, name='rute_page'),
    url(r'^pois/create/$', create_poi, name='create_poi')

]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
