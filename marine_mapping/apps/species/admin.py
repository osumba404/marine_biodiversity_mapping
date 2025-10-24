from django.contrib import admin
from .models import Species, Occurrence


@admin.register(Species)
class SpeciesAdmin(admin.ModelAdmin):
    list_display = ("scientific_name", "common_name", "iucn_status", "source")
    search_fields = ("scientific_name", "common_name", "taxon_id")


@admin.register(Occurrence)
class OccurrenceAdmin(admin.ModelAdmin):
    list_display = ("species", "observed_at", "verified", "source")
    list_filter = ("verified", "source")
    search_fields = ("species__scientific_name", "source_id")
