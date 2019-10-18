from django.core.serializers import serialize
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.gis.geos import GEOSGeometry

from chartjs.views.lines import BaseLineChartView
from django.views.generic import DetailView

# Create your views here.
from django.views.generic import TemplateView

from .models import (Punct_de_interes, Canal, Suprafata, Tura, Ruta,
                     CoteDunare, TipPOI)


class HomePageView(TemplateView):
    template_name = 'index.html'


def create_poi(request):
    if request.method == 'POST':
        # location = request.POST['location']
        lat = request.POST['lat']
        long = request.POST['long']
        # request.POST['poi_type']
        poi_type = TipPOI.objects.get(name=request.POST["poi_type"])

        Punct_de_interes.objects.create(
            # location=Point(lat, long, srid=4326),
            location=GEOSGeometry('POINT(%s %s)' % (long, lat), srid=4326),
            poi_type=poi_type,
        )

        pois = serialize('geojson', Punct_de_interes.objects.all())
        # return render(request=request,
        #               template_name='pois.html',
        #               context={'pois': pois}
        #               )
        return HttpResponse(pois, content_type='json')


def poi_datasets(request):
    pois = serialize('geojson', Punct_de_interes.objects.all())
    return HttpResponse(pois, content_type='json')


def asezari_datasets(request):
    asezari = serialize('geojson', Punct_de_interes.objects.filter(poi_type__name__contains='așezare'))
    return HttpResponse(asezari, content_type='json')


def pensiune_datasets(request):
    pensiune = serialize('geojson', Punct_de_interes.objects.filter(poi_type__name__contains='pensiune'))
    return HttpResponse(pensiune, content_type='json')


def arbori_datasets(request):
    arbore = serialize('geojson', Punct_de_interes.objects.filter(poi_type__name__contains='arbore'))
    return HttpResponse(arbore, content_type='json')


def localitate_datasets(request):
    localitate = serialize('geojson', Punct_de_interes.objects.filter(poi_type__name__contains='localitate'))
    return HttpResponse(localitate, content_type='json')


def pescuit_datasets(request):
    pescuit = serialize('geojson', Punct_de_interes.objects.filter(poi_type__name__contains='pescuit'))
    return HttpResponse(pescuit, content_type='json')


def colonie_datasets(request):
    colonie = serialize('geojson', Punct_de_interes.objects.filter(poi_type__name__contains='colonie'))
    return HttpResponse(colonie, content_type='json')


def apascazuta_datasets(request):
    apascazuta = serialize('geojson', Punct_de_interes.objects.filter(poi_type__name__contains='apă'))
    return HttpResponse(apascazuta, content_type='json')


def vegetatie_datasets(request):
    vegetatie = serialize('geojson', Punct_de_interes.objects.filter(poi_type__name__contains='vegetație'))
    return HttpResponse(vegetatie, content_type='json')


def punctlansare_datasets(request):
    punctlansare = serialize('geojson', Punct_de_interes.objects.filter(poi_type__name__contains='punct'))
    return HttpResponse(punctlansare, content_type='json')


def camping_datasets(request):
    camping = serialize('geojson', Punct_de_interes.objects.filter(poi_type__name__contains='camping'))
    return HttpResponse(camping, content_type='json')


def colmatat_datasets(request):
    colmatat = serialize('geojson', Punct_de_interes.objects.filter(poi_type__name__contains='colmatat'))
    return HttpResponse(colmatat, content_type='json')


def grind_datasets(request):
    grinduri = serialize('geojson', Suprafata.objects.filter(type_id__name__contains='grind'))
    return HttpResponse(grinduri, content_type='json')


def padure_datasets(request):
    paduri = serialize('geojson', Suprafata.objects.filter(type_id__name__contains='pădure'))
    return HttpResponse(paduri, content_type='json')


def ariiprotejate_datasets(request):
    arii = serialize('geojson', Suprafata.objects.filter(type_id__name__contains='strict'))
    return HttpResponse(arii, content_type='json')


def canale_datasets(request):
    var_canal = serialize('geojson', Canal.objects.all())
    return HttpResponse(var_canal, content_type='json')


def afisare_ture(request):
    return render(request=request,
                  template_name="ture.html",
                  context={"ture": Tura.objects.all()})


class LineChartJSONView(BaseLineChartView):

    def get_labels(self):
        """Return 7 labels for the x-axis."""
        # return ["January", "February", "March", "April", "May", "June"]

        label = [cd.data_actualizare.strftime("%d %b") for cd in CoteDunare.objects.all()]
        return label

    def get_providers(self):
        """Return names of datasets."""
        return ["Nivelul Apei", "Temperatura"]

    def get_data(self):
        """Return 3 datasets to plot."""
        apa = [cd.nivelul_apei for cd in CoteDunare.objects.all()]
        temp = [cd.temp_masurata for cd in CoteDunare.objects.all()]
        # var_data = json.dumps([apa, temp])
        return [apa, temp]

        # return [[75, 44, 92, 11, 44, 95],
        #         [87, 21, 94, 3, 90, 13]]


line_chart = TemplateView.as_view(template_name='DDGraph.html')
line_chart_json = LineChartJSONView.as_view()


class RutaDetailView(DetailView):
    queryset = Ruta.objects.all()


def rute_tura(request, id_tura):
    try:
        tura = Tura.objects.get(pk=id_tura)
    except Tura.DoesNotExist:
        return HttpResponse("{}", content_type="json")
    else:
        rute = serialize("geojson", tura.routes.all())
        return HttpResponse(rute, content_type="json")
