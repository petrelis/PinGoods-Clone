# Generated by Django 3.2.8 on 2021-11-24 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0008_auto_20211116_1222'),
    ]

    operations = [
        migrations.AddField(
            model_name='offer',
            name='offer_image',
            field=models.ImageField(default='default.jpg', upload_to='offer_pics'),
        ),
    ]
