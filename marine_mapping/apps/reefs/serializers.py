from rest_framework_gis.serializers import GeoFeatureModelSerializer
from .models import ReefSite


class ReefSiteGeoSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = ReefSite
        geo_field = 'geometry'
        fields = (
            'id', 'name', 'reef_type', 'condition_score', 'source', 'metadata',
        )
