from django.contrib.gis import admin
from django.contrib.gis.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class City(models.Model):
    name = models.CharField(max_length=30)
    point = models.PointField()

    objects = models.GeoManager()

    class Meta:
        app_label = 'geoadmin'

    def __str__(self):
        return self.name

site = admin.AdminSite(name='admin_gis')
site.register(City, admin.OSMGeoAdmin)
