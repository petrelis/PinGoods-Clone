# Generated by Django 3.2.8 on 2021-12-11 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0009_offer_offer_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='offer',
            name='offer_coords_lat',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='offer',
            name='offer_coords_lng',
            field=models.FloatField(default=0),
        ),
    ]
