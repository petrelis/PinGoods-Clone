# Generated by Django 3.2.8 on 2021-10-30 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_profile_email1'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='email1',
        ),
        migrations.AddField(
            model_name='profile',
            name='email',
            field=models.EmailField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='phone',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]
