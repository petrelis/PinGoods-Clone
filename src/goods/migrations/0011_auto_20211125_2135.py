# Generated by Django 3.2.9 on 2021-11-25 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0010_auto_20211125_2106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer',
            name='offer_coords_lat',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='offer',
            name='offer_coords_lng',
            field=models.FloatField(),
        ),
    ]
