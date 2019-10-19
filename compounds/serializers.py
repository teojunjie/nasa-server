from rest_framework.serializers import (
    ModelSerializer,
    CharField,
    CharField,
    DateTimeField,
    CharField,
)

from .models import Compound

class CompoundSerializer(ModelSerializer):
    melting_point = CharField()
    boiling_point = CharField()
    molecular_weight = CharField()

    class Meta:
        model = Compound
        fields = '__all__'