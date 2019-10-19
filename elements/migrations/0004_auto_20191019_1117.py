# Generated by Django 2.2.5 on 2019-10-19 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elements', '0003_auto_20191019_1110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='element',
            name='atomic_number',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='element',
            name='atomic_radius',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='element',
            name='boiling_point',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='element',
            name='density',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='element',
            name='electron_affinity',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='element',
            name='electronegativity',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='element',
            name='melting_point',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='element',
            name='van_der_waal_radius',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='element',
            name='year_discovered',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
