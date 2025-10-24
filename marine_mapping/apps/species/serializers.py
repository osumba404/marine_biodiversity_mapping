from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer
from .models import Species, Occurrence


class SpeciesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Species
        fields = (
            'id', 'scientific_name', 'common_name', 'taxon_id',
            'iucn_status', 'source', 'metadata', 'created_at', 'updated_at'
        )


class OccurrenceGeoSerializer(GeoFeatureModelSerializer):
    species_name = serializers.CharField(source='species.scientific_name', read_only=True)

    class Meta:
        model = Occurrence
        geo_field = 'location'
        fields = (
            'id', 'species', 'species_name', 'observed_at', 'photo_url',
            'source', 'source_id', 'verified', 'quality_score', 'metadata'
        )
