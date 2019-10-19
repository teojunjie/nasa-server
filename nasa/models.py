from django.db import models

    
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
    )
    solarEvent = models.ForeignKey(
        SolarFlare,
        on_delete= models.CASCADE
    )
