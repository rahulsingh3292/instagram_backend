import uuid

from django.contrib.gis.db import models as gis_models
from django.db import models

__all__ = ['LocationMixin', 'PrimaryKeyMixin',]


class LocationMixin(gis_models.Model):
    location = gis_models.PointField(srid=4326, blank=True, null=True)

    class Meta:
        abstract = True


class PrimaryKeyMixin(models.Model):
    id = models.UUIDField(primary_key=True, db_index=True,
                          serialize=False, default=uuid.uuid4)

    class Meta:
        abstract = True
