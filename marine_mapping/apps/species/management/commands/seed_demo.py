from django.core.management.base import BaseCommand
from django.utils import timezone
from django.contrib.gis.geos import Point, Polygon, MultiPolygon

from apps.species.models import Species, Occurrence
from apps.reefs.models import ReefSite


class Command(BaseCommand):
    help = "Seed demo reef polygons and species occurrences for the Kenyan coast"

    def handle(self, *args, **options):
        # Create a couple of species
        acropora, _ = Species.objects.get_or_create(
            scientific_name="Acropora digitifera",
            defaults={
                "common_name": "Staghorn coral",
                "iucn_status": "NT",
                "source": "demo",
            },
        )
        parrotfish, _ = Species.objects.get_or_create(
            scientific_name="Scarus ghobban",
            defaults={
                "common_name": "Blue-barred parrotfish",
                "iucn_status": "LC",
                "source": "demo",
            },
        )

        # Create a couple of simple reef polygons (approximate boxes) near the Kenyan coast
        # Reef 1 near Mombasa
        poly1 = Polygon((
            (39.60, -4.10),
            (39.75, -4.10),
            (39.75, -4.00),
            (39.60, -4.00),
            (39.60, -4.10),
        ))
        # Reef 2 near Malindi/Watamu
        poly2 = Polygon((
            (39.95, -3.45),
            (40.10, -3.45),
            (40.10, -3.30),
            (39.95, -3.30),
            (39.95, -3.45),
        ))

        reef1, _ = ReefSite.objects.get_or_create(
            name="Mombasa Reef Area (Demo)",
            defaults={
                "geometry": MultiPolygon(poly1, srid=4326),
                "reef_type": "fringing",
                "condition_score": 0.6,
                "source": "demo",
            },
        )
        reef2, _ = ReefSite.objects.get_or_create(
            name="Watamu Reef Area (Demo)",
            defaults={
                "geometry": MultiPolygon(poly2, srid=4326),
                "reef_type": "patch",
                "condition_score": 0.7,
                "source": "demo",
            },
        )

        # Occurrences (verified) near those reefs
        occ_points = [
            (acropora, Point(39.68, -4.05, srid=4326)),
            (parrotfish, Point(39.70, -4.03, srid=4326)),
            (acropora, Point(40.02, -3.38, srid=4326)),
            (parrotfish, Point(40.05, -3.34, srid=4326)),
        ]
        created = 0
        for species, pt in occ_points:
            obj, was_created = Occurrence.objects.get_or_create(
                species=species,
                location=pt,
                observed_at=timezone.now().date(),
                defaults={
                    "source": "demo",
                    "source_id": "demo",
                    "verified": True,
                    "quality_score": 0.9,
                },
            )
            if was_created:
                created += 1

        self.stdout.write(self.style.SUCCESS(
            f"Seed complete: species={Species.objects.count()}, reefs={ReefSite.objects.count()}, new_occurrences={created}"
        ))
