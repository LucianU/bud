from __future__ import unicode_literals

import datetime

from django.contrib.gis.db import models
from django.contrib.auth.models import User
from colorful.fields import RGBColorField

# Create your models here.
from django.urls import reverse


class TipPOI(models.Model):
    name = models.CharField(max_length=35)
    icon = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Tipuri POI'


class Punct_de_interes(models.Model):
    name = models.CharField(max_length=35, blank=True, null=True, default="Nu e disponibil")
    location = models.PointField(srid=4326)
    poi_type = models.ForeignKey(TipPOI, on_delete=models.CASCADE, default=1, related_name='puncte_de_interes')
    image = models.ImageField(upload_to='imagini_poi',default='imagini_ture/bors_de_peste.jpg')
    telephone = models.CharField(max_length=15, blank=True, null=True, default="N/A")
    objects = models.Manager()
    date_created = models.DateField(default=datetime.date.today)
    date_modified = models.DateField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Puncte de interes'


class Canal(models.Model):
    osm_id = models.BigIntegerField()
    name = models.CharField(max_length=48)
    type = models.CharField(max_length=16)
    width = models.IntegerField()
    geom = models.MultiLineStringField(srid=4326)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Canale'


class TipSuprafata(models.Model):
    name = models.CharField(max_length=80)
    color = RGBColorField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Tipuri suprafete'


class Suprafata(models.Model):
    objectid = models.BigIntegerField()
    name = models.CharField(max_length=80)
    type_id = models.ForeignKey(TipSuprafata, on_delete=models.CASCADE, related_name='suprafete')
    geom = models.MultiPolygonField(srid=4326)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Suprafete'


class CoteDunare(models.Model):
    oras = models.CharField(max_length=48, default="Tulcea")
    km = models.IntegerField(default=71)
    nivelul_apei = models.IntegerField()
    variatia =  models.IntegerField(blank=True, null=True)
    temp_masurata =  models.FloatField()
    data_actualizare = models.DateField()

    def __str__(self):
        return self.oras

    class Meta:
        verbose_name_plural = 'CoteDunare'


class Ruta(models.Model):
    name = models.CharField(max_length=48)
    start_point = models.CharField(max_length=48)
    end_point = models.CharField(max_length=48)
    distance = models.IntegerField()
    difficulty = models.CharField(max_length=20)
    geom = models.MultiLineStringField(srid=4326)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('ruta-detail', args=[str(self.id)])

    class Meta:
        verbose_name_plural = 'Rute'


class Tura(models.Model):
    DIFFICULTY_CHOICES = (
        (0, u'usor'),
        (1, u'intermediar'),
        (2, u'greu'),
    )
    name = models.CharField(max_length=48)
    description = models.CharField(max_length=500, default='demo description')
    image = models.ImageField(upload_to='imagini_ture',default='imagini_ture/bors_de_peste.jpg')
    difficulty = models.SmallIntegerField(choices=DIFFICULTY_CHOICES)
    PRIVACY_CHOICES = (
        (0, u'privat'),
        (1, u'public'),
    )
    privacy = models.SmallIntegerField(choices=PRIVACY_CHOICES, default=1, blank=True)
    routes = models.ManyToManyField('Ruta')

    def __str__(self):
        return self.name

    @property
    def no_days(self):
        return sum(n.no_days for n in self.routes.all())

    @property
    def total_distance(self):
        return sum(n.total_distance for n in Ruta.distance.all())

    class Meta:
        verbose_name_plural = 'Ture'

# class Profile(models.Model):
#     GENDER_CHOICES = (
#         ('male', 'Male'),
#         ('female', 'Female'),
#     )
#     user = models.OneToOneField(User)
#     picture = models.ImageField(upload_to='profiles', blank=True, null=True)
#     description = models.TextField(blank=True, null=True)
#     name = models.CharField(max_length=255, blank=True, null=True)
#     gender = models.CharField(max_length=6, choices=GENDER_CHOICES,
#                               blank=True, null=True)
#     location = models.CharField(max_length=255, blank=True, null=True)
#
#     @models.permalink
#     def get_absolute_url(self):
#         return reverse('user_home', (self.user.id,))
