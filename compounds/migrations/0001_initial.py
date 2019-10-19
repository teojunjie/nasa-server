# Generated by Django 2.2.5 on 2019-10-19 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Compound',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('melting_point', models.CharField(max_length=255)),
                ('boiling_point', models.CharField(max_length=255)),
                ('molecular_weight', models.CharField(max_length=255)),
            ],
        ),
    ]
