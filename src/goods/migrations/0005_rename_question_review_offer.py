# Generated by Django 3.2.8 on 2021-11-08 16:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0004_review_author'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='question',
            new_name='offer',
        ),
    ]