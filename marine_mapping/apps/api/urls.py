from rest_framework.routers import DefaultRouter
from django.urls import path, include

from apps.species.views import SpeciesViewSet, OccurrenceViewSet
from apps.reefs.views import ReefSiteViewSet

router = DefaultRouter()
router.register(r'species', SpeciesViewSet, basename='species')
router.register(r'occurrences', OccurrenceViewSet, basename='occurrence')
router.register(r'reefs', ReefSiteViewSet, basename='reef')

urlpatterns = [
    path('', include(router.urls)),
]
