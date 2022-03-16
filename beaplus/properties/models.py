"""Properties models."""

# Django
from django.db import models
from django.conf import settings 
from django.core.validators import RegexValidator

# Utilities
from beaplus.utils.models import BPModel

class Property(BPModel):
    """Property model."""

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) 
    name = models.CharField(max_length = 50)
    location = models.CharField(max_length = 50)

    # Coordinates
    latitude = models.DecimalField(max_digits=19, decimal_places=10)
    longitude = models.DecimalField(max_digits=19, decimal_places=10)

    # Energy
    energy_certificate = models.CharField(max_length = 10, blank=True, null=True)
    windows =  models.CharField(max_length = 50, blank=True, null=True)
    ventilation = models.CharField(max_length = 50, blank=True, null=True)
    solar_protection = models.CharField(max_length = 50, blank=True, null=True)
    installations = models.CharField(max_length = 50, blank=True, null=True)
    ilumination_energy = models.CharField(max_length = 50, blank=True, null=True)

    # Health and Wellness
    humidity =  models.CharField(max_length = 50, blank=True, null=True)
    acoustic = models.CharField(max_length = 50, blank=True, null=True)
    illumination_health = models.CharField(max_length = 50, blank=True, null=True)
    air_quality = models.CharField(max_length = 50, blank=True, null=True)
    parkland = models.CharField(max_length = 50, blank=True, null=True)
    construction_materials = models.CharField(max_length = 50, blank=True, null=True)

    # Social comfort
    accessibility = models.CharField(max_length = 50, blank=True, null=True)
    quality_spaces = models.CharField(max_length = 50, blank=True, null=True)
    views = models.CharField(max_length = 50, blank=True, null=True)
    digitization = models.CharField(max_length = 50, blank=True, null=True) 



    def __str__(self):
        """Return first name and user name."""
        return '{} by @{}'.format(self.name, self.user.username)
    
    class Meta:
        verbose_name_plural = "Properties"

class PropertyPhoto(BPModel):
    """Property photo model."""

    property = models.ForeignKey(Property, on_delete=models.CASCADE) 
    name = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='photos')

    def __str__(self):
        """Return name and property."""
        return '{} by @{}'.format(self.name, self.property)