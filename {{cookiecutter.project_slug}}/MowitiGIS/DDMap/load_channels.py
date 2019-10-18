import os
from django.contrib.gis.utils import LayerMapping
from .models import Canal

canale_mapping = {
    'osm_id': 'osm_id',
    'name': 'name',
    'type': 'type',
    'width': 'width',
    'geom': 'MULTILINESTRING',
}

canal_shp = os.path .abspath(os.path.join(os.path.dirname(__file__), 'data/ro_waterways/canale_delta.shp'))


def run(verbose=True):
    lm = LayerMapping(Canal, canal_shp, canale_mapping, transform=False, encoding='iso-8859-1')
    lm.save(strict=True, verbose=verbose)
