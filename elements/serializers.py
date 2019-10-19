from rest_framework.serializers import (
    ModelSerializer,
    CharField,
    CharField,
    DateTimeField,
    CharField,
)

from .models import Element

class ElementSerializer(ModelSerializer):
    atomic_mass = CharField()
    atomic_number = CharField()
    atomic_radius = CharField()
    boiling_point = CharField()
    bonding_type = CharField()
    cpk_hex_color = CharField()
    density = CharField()
    electron_affinity = CharField()
    electronegativity = CharField()
    electronic_configuration = CharField()
    group_block = CharField()
    ion_radius = CharField()
    ionization_energy = CharField()
    melting_point = CharField()
    name = CharField()
    oxidation_states = CharField()
    standard_state = CharField()
    symbol = CharField()
    van_der_waal_radius = CharField()
    year_discovered = CharField()

    class Meta:
        model = Element
        fields = '__all__'
