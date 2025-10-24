from django.contrib.gis.db import models


class Species(models.Model):
    scientific_name = models.CharField(max_length=255)
    common_name = models.CharField(max_length=255, blank=True)
    taxon_id = models.CharField(max_length=100, blank=True, null=True)
    iucn_status = models.CharField(max_length=50, blank=True)
    source = models.CharField(max_length=255, blank=True)
    metadata = models.JSONField(default=dict, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.scientific_name


class Occurrence(models.Model):
    species = models.ForeignKey(Species, on_delete=models.CASCADE, related_name='occurrences')
    location = models.PointField(srid=4326)
    observed_at = models.DateField(null=True, blank=True)
    source = models.CharField(max_length=255, blank=True)
    source_id = models.CharField(max_length=255, blank=True)
    photo_url = models.URLField(blank=True)
    verified = models.BooleanField(default=False)
    quality_score = models.FloatField(default=0)
    metadata = models.JSONField(default=dict, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.species.scientific_name} @ {self.location.y:.4f},{self.location.x:.4f}"
