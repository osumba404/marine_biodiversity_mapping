from django.contrib import admin
from .models import ReefSite


@admin.register(ReefSite)
class ReefSiteAdmin(admin.ModelAdmin):
    list_display = ("name", "reef_type", "condition_score", "source")
    search_fields = ("name",)
