# Generated by Django 3.2.8 on 2021-11-08 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0006_review_pub_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='offer',
            name='offer_address',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AddField(
            model_name='offer',
            name='offer_phonenumber',
            field=models.CharField(blank=True, max_length=15),
        ),
    ]
