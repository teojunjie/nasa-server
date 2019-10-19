from django.db import models

NASA_EVENTS = [
    ('solar', 'solarFlare'),
]

class SolarFlare(models.Model):
    classType = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )
    datetime = models.DateTimeField()
    name = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )

class NasaEvent(models.Model):
    event = models.CharField(
        max_length=255,
        null=False,
        blank=False,
        choices=NASA_EVENTS,
    )
    solarEvent = models.ForeignKey(
        SolarFlare,
        on_delete= models.CASCADE,
        null=True,
    )

class SolarBody(models.Model):
    englishName = models.CharField(
        max_length=255,
        db_index=True,
        null=False,
        blank=False,
    )
    isPlanet = models.BooleanField(
        null=False,
    )
    dimension = models.CharField(
        max_length=255,
        null=True, 
        default=None,
    )
    gravity = models.FloatField(
        null=True, 
        blank=True, 
        default=None,
    )
    meanRadius = models.FloatField(
        null=True, 
        blank=True, 
        default=None,
    )
