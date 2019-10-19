from rest_framework.serializers import (
    ModelSerializer,
    CharField,
    IntegerField,
    DateTimeField,
    FloatField,
    BooleanField,
)

from .models import (
    SolarFlare,
    NasaEvent,
    SolarBody,
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
    
class SolarBodySerializer(ModelSerializer):
    englishName = CharField()
    isPlanet = BooleanField()
    dimension = CharField()
    gravity = FloatField()
    meanRadius = FloatField()

    class Meta:
        model = SolarBody
        fields = '__all__'