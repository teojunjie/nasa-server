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
