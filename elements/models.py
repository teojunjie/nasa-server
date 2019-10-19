from django.db import models

class Element(models.Model):
    atomic_mass = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )
    atomic_number = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )
    atomic_radius = models.IntegerField(
        max_length=255,
        null=True,
        blank=True,
    )
    boiling_point = models.IntegerField(
        null=True,
        blank=True,
    )
    bonding_type = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )
    cpk_hex_color = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )
    density = models.FloatField(
        null=True,
        blank=True,
    )
    electron_affinity = models.IntegerField(
        null=True,
        blank=True,
    )
    electronegativity = models.FloatField(
        null=True,
        blank=True,
    )
    electronic_configuration = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )
    group_block = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )
    ion_radius = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )
    ionization_energy = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )
    melting_point = models.IntegerField(
        null=True,
        blank=True,
    )
    name = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )
    oxidation_states = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )
    standard_state = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )
    symbol = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )
    van_der_waal_radius = models.IntegerField(
        null=True,
        blank=True,
    )
    year_discovered = models.IntegerField(
        null=True,
        blank=True,
    )
