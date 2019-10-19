from django.db import models
from nasa.models import NasaEvent

class Trivial(models.Model):
    fact = models.CharField(
        max_length=10000,
        blank=False,
        null=False,
    )
    date = models.DateTimeField()
    nasa_event = models.ForeignKey(
        NasaEvent,
        on_delete=models.PROTECT,
    )
    

