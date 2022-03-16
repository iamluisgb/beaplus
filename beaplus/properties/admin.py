"""Properties model admin."""

# Django
from django.contrib import admin

# Models
from beaplus.properties.models import Property, PropertyPhoto


@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    """Property admin."""
    
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

@admin.register(PropertyPhoto)
class PropertyPhotoAdmin(admin.ModelAdmin):
    """Property Photo admin."""

    list_display = ('id', 'property', 'photo')
    search_fields = ('property',)
    list_filter = ('created', 'modified')