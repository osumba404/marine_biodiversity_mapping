from django.contrib.gis.db import models


class ReefSite(models.Model):
    name = models.CharField(max_length=255)
    geometry = models.MultiPolygonField(srid=4326)
    reef_type = models.CharField(max_length=100, blank=True)
    condition_score = models.FloatField(default=0)
    source = models.CharField(max_length=255, blank=True)
    metadata = models.JSONField(default=dict, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name or "ReefSite"
