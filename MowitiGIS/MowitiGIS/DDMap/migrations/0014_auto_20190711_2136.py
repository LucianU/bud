# Generated by Django 2.2.1 on 2019-07-11 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DDMap', '0013_auto_20190711_1832'),
    ]

    operations = [
        migrations.AlterField(
            model_name='punct_de_interes',
            name='telephone',
            field=models.CharField(blank=True, default='N/A', max_length=15, null=True),
        ),
    ]
