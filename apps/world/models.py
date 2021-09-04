import uuid
from django.contrib.gis.db import models


class Country(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    external_id = models.CharField(max_length=250, db_index=True, null=True, blank=True)
    name = models.CharField(max_length=100, db_index=True, null=False, blank=False)
    iso_code = models.CharField(max_length=10, db_index=True, null=False, blank=False)
    geom = models.GeometryField(null=False, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True, null=False)
    updated_at = models.DateTimeField(auto_now=True, null=False)

    class Meta:
        verbose_name = 'Country'
        verbose_name_plural = 'Countries'
