from rest_framework.serializers import (
    ModelSerializer,
    CharField,
    IntegerField,
    DateTimeField,
)

from nasa.serializers import NasaEventSerializer
from trivial.models import Trivial

class TrivialSerializer(ModelSerializer):
  fact = CharField()
  date = DateTimeField()
  nasa_event = NasaEventSerializer()

  class Meta: 
    model = Trivial 
    fields = "__all__"
