from rest_framework.permissions import AllowAny
from rest_framework import viewsets

from .models import ReefSite
from .serializers import ReefSiteGeoSerializer


class ReefSiteViewSet(viewsets.ModelViewSet):
    queryset = ReefSite.objects.all()
    serializer_class = ReefSiteGeoSerializer
    permission_classes = [AllowAny]
