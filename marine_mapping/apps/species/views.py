from rest_framework import viewsets, mixins
from rest_framework.permissions import AllowAny
from rest_framework_gis.viewsets import GeoModelViewSet

from .models import Species, Occurrence
from .serializers import SpeciesSerializer, OccurrenceGeoSerializer


class SpeciesViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Species.objects.all().order_by('scientific_name')
    serializer_class = SpeciesSerializer
    permission_classes = [AllowAny]


class OccurrenceViewSet(GeoModelViewSet):
    queryset = Occurrence.objects.filter(verified=True)
    serializer_class = OccurrenceGeoSerializer
    permission_classes = [AllowAny]
