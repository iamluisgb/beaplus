"""Properties model admin."""

# Django
from django.contrib import admin

# Models
from beaplus.properties.models import Property


@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    """Property admin."""

    """list_display = ('id', 'user', 'name', 'location', 'energy_certificate', 
    'windows', 'ventilation', 'solar_protection', 'installations', 'ilumination',
    'humidity', 'acoustic', 'illumination', 'air_quality', 'parkland', 'construction_materials',
    'accessibility', 'quality_spaces', 'views', 'digitization')"""
    
    fieldsets = (
        ( None, {
            'fields': ('user', 'name', 'location', 'latitude', 'longitude'),
        }),
        ('Energy', {
            'classes': ('collapse',),
            'fields': ('energy_certificate', 
            'windows', 'ventilation', 'solar_protection', 'installations', 'ilumination_energy'),
            }),
            ('Health and wellness', {
            'classes': ('collapse',),
            'fields': ('humidity', 'acoustic', 'illumination_health', 'air_quality', 'parkland'),
            }),
            ('Social comfort', {
            'classes': ('collapse',),
            'fields': ('accessibility', 'quality_spaces', 'views', 'digitization'),
            }),
    )
    
    list_filter = ('created', 'modified')