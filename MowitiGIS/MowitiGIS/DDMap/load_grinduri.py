import os
from django.contrib.gis.utils import LayerMapping
from .models import Suprafata

grinduri_mapping = {
    'objectid': 'OBJECTID',
    'name': 'NAME',
    'geom': 'MULTIPOLYGON',
   }

grind_shp = os.path .abspath(os.path.join(os.path.dirname(__file__), 'data/grinduri/grinduri.shp'))


def run(verbose=True):
    lm = LayerMapping(Suprafata, grind_shp, grinduri_mapping, transform=False, encoding='iso-8859-1')
    lm.save(strict=True, verbose=verbose)
