from django.db import models

class Compound(models.Model):
    name = models.CharField(
        max_length=255,
        null=False,
        blank=False,
    )
    melting_point = models.CharField(
        max_length=255,
        null=False,
        blank=False,
    )
    boiling_point = models.CharField(
        max_length=255,
        null=False,
        blank=False,
    )
    molecular_weight = models.CharField(
        max_length=255,
        null=False,
        blank=False,
    )