# Generated by Django 3.2.8 on 2021-10-30 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='email1',
            field=models.EmailField(blank=True, max_length=150),
        ),
    ]
