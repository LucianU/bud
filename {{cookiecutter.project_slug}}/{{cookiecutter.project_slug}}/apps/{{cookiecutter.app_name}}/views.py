from django.core.serializers import serialize
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import DetailView
{% if cookiecutter.GIS_project == "y" %}
from django.contrib.gis.geos import GEOSGeometry
{% endif %}

from django.views.generic import TemplateView

# Create your views here.
class HomePageView(TemplateView):
    template_name = '{{cookiecutter.app_name}}/home.html'