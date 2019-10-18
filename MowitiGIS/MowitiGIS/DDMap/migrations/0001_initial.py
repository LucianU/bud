# Generated by Django 2.2.1 on 2019-07-07 06:36

import colorful.fields
import datetime
import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Canal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('osm_id', models.BigIntegerField()),
                ('name', models.CharField(max_length=48)),
                ('type', models.CharField(max_length=16)),
                ('width', models.IntegerField()),
                ('geom', django.contrib.gis.db.models.fields.MultiLineStringField(srid=4326)),
            ],
            options={
                'verbose_name_plural': 'Canale',
            },
        ),
        migrations.CreateModel(
            name='CoteDunare',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('oras', models.CharField(max_length=48)),
                ('km', models.IntegerField()),
                ('nivelul_apei', models.IntegerField()),
                ('variatia', models.IntegerField()),
                ('temp_masurata', models.FloatField()),
                ('data_actualizare', models.DateField()),
            ],
            options={
                'verbose_name_plural': 'CoteDunare',
            },
        ),
        migrations.CreateModel(
            name='Ruta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=48)),
                ('start_point', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('end_point', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('distance', models.IntegerField()),
                ('difficulty', models.CharField(max_length=20)),
                ('geom', django.contrib.gis.db.models.fields.MultiLineStringField(srid=4326)),
            ],
            options={
                'verbose_name_plural': 'Rute',
            },
        ),
        migrations.CreateModel(
            name='TipPOI',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=35)),
                ('icon', models.ImageField(blank=True, null=True, upload_to='')),
            ],
            options={
                'verbose_name_plural': 'Tipuri POI',
            },
        ),
        migrations.CreateModel(
            name='TipSuprafata',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('objectid', models.BigIntegerField()),
                ('name', models.CharField(max_length=80)),
                ('color', colorful.fields.RGBColorField()),
            ],
            options={
                'verbose_name_plural': 'Tipuri suprafete',
            },
        ),
        migrations.CreateModel(
            name='Tura',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=48)),
                ('difficulty', models.SmallIntegerField(choices=[(0, 'easy'), (1, 'intermediate'), (2, 'hard')])),
                ('privacy', models.SmallIntegerField(blank=True, choices=[(0, 'private'), (1, 'public')], default=1)),
                ('routes', models.ManyToManyField(to='DDMap.Ruta')),
            ],
            options={
                'verbose_name_plural': 'Ture',
            },
        ),
        migrations.CreateModel(
            name='Suprafata',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('objectid', models.BigIntegerField()),
                ('name', models.CharField(max_length=80)),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
                ('type_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DDMap.TipSuprafata')),
            ],
            options={
                'verbose_name_plural': 'Suprafete',
            },
        ),
        migrations.CreateModel(
            name='Punct_de_interes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=35)),
                ('location', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('date_created', models.DateField(default=datetime.date.today)),
                ('date_modified', models.DateField(auto_now=True)),
                ('poi_type', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='DDMap.TipPOI')),
            ],
            options={
                'verbose_name_plural': 'Puncte de interes',
            },
        ),
    ]
