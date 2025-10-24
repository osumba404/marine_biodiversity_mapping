from rest_framework.permissions import AllowAny
from rest_framework_gis.viewsets import GeoModelViewSet

from .models import ReefSite
from .serializers import ReefSiteGeoSerializer


class ReefSiteViewSet(GeoModelViewSet):
    queryset = ReefSite.objects.all()
    serializer_class = ReefSiteGeoSerializer
    permission_classes = [AllowAny]
