# Generated by Django 3.2.7 on 2021-09-04 13:17

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('world', '0002_alter_country_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='country',
            name='geom',
            field=django.contrib.gis.db.models.fields.MultiPolygonField(db_index=True, srid=4326),
        ),
    ]
