import io
import os
import zipfile
from urllib import request
from django.conf import settings
from django.contrib.gis.gdal import DataSource
from django.contrib.gis.utils import LayerMapping
from django.core.management.base import BaseCommand, CommandError
from apps.world import models

class Command(BaseCommand):
    help = 'Import models'

    def add_arguments(self, parser):
        parser.add_argument(
            'type',
            type=str,
            choices=['world'],
        )

    def handle(self, *args, **options):
        print(f"Let's import {options['type']} models")
        dest = os.path.join(settings.BASE_DIR, 'temp', options['type'])

        if options['type'] == 'world':
            url = "https://thematicmapping.org/downloads/TM_WORLD_BORDERS-0.3.zip"

        # elif options['type'] == 'country':
        #     url = f"https://biogeo.ucdavis.edu/data/gadm3.6/gpkg/gadm36_{options['code']}_gpkg.zip"

        else:
            raise Exception('Incorrect type selected')

        # Extract file
        response = request.Request(url, headers=self.get_headers())
        pagedata = request.urlopen(response)
        zip = zipfile.ZipFile(io.BytesIO(pagedata.read()))
        zip.extractall(dest)

        lm = LayerMapping(
            models.Country,
            dest,
            {
                'fips' : 'FIPS',
                'iso2' : 'ISO2',
                'iso3' : 'ISO3',
                'un' : 'UN',
                'name' : 'NAME',
                'area' : 'AREA',
                'region' : 'REGION',
                'subregion' : 'SUBREGION',
                'lon' : 'LON',
                'lat' : 'LAT',
                'geom' : 'MULTIPOLYGON',
            },
            transform=False,
        )
        lm.save(strict=True, verbose=options['verbosity'])


    def get_headers(self):
        return {
            'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-encoding': 'gzip, deflate, br',
        }