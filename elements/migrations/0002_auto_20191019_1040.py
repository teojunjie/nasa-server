# Generated by Django 2.2.5 on 2019-10-19 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elements', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='element',
            name='atomic_radius',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]