# Generated by Django 2.2.5 on 2019-10-19 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elements', '0002_auto_20191019_1040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='element',
            name='atomic_number',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
