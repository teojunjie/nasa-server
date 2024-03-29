# Generated by Django 2.2.5 on 2019-10-19 10:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('nasa', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nasaevent',
            name='event',
            field=models.CharField(choices=[('solar', 'solarFlare')], max_length=255),
        ),
        migrations.AlterField(
            model_name='nasaevent',
            name='solarEvent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='nasa.SolarFlare'),
        ),
        migrations.AlterField(
            model_name='solarflare',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True, unique=True),
        ),
    ]
