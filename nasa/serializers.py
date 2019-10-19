from rest_framework.serializers import (
    ModelSerializer,
    CharField,
    IntegerField,
    DateTimeField,
)

from .models import (
    SolarFlare,
    NasaEvent,
)

class SolarFlareSerializer(ModelSerializer):
    classType = CharField()
    datetime = DateTimeField()
    name = CharField()
    
    class Meta:
        model = SolarFlare
        fields = '__all__'

class NasaEventSerializer(ModelSerializer):
    event = CharField()
    solarEvent = SolarFlareSerializer()

    class Meta:
        model = NasaEvent
        fields = '__all__'
    