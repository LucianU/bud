# Generated by Django 2.2.1 on 2019-07-09 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DDMap', '0009_punct_de_interes_telephone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='punct_de_interes',
            name='image',
            field=models.ImageField(default='imagini_ture/bors_de_peste.jpg', upload_to='imagini_poi'),
        ),
    ]
