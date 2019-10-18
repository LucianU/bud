from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin
# Register your models here.
from .models import Punct_de_interes, Canal, CoteDunare, Suprafata, TipSuprafata, TipPOI, Ruta, Tura


class TipPoiAdmin(LeafletGeoAdmin):
    list_display = ('name', 'icon')


class PoiAdmin(LeafletGeoAdmin):
    list_display = ('name', 'location', 'poi_type')


class ChannelAdmin(LeafletGeoAdmin):
    list_display = ('name', 'type')


class TipSuprafAdmin(LeafletGeoAdmin):
    list_display = ('name', 'color')


class SuprafeteAdmin(LeafletGeoAdmin):
    list_display = ('name', 'geom')


class CoteAdmin(LeafletGeoAdmin):
    list_display = ('oras', 'nivelul_apei','temp_masurata','data_actualizare')


class RutaAdmin(LeafletGeoAdmin):
    list_display = ('name', 'start_point','end_point','geom')


class TuraAdmin(LeafletGeoAdmin):
    list_display = ('name', 'difficulty', 'privacy')


admin.site.register(TipPOI, TipPoiAdmin)
admin.site.register(Punct_de_interes, PoiAdmin)
admin.site.register(Canal, ChannelAdmin)
admin.site.register(TipSuprafata, TipSuprafAdmin)
admin.site.register(Suprafata, SuprafeteAdmin)
admin.site.register(CoteDunare, CoteAdmin)
admin.site.register(Ruta, RutaAdmin)
admin.site.register(Tura, TuraAdmin)
