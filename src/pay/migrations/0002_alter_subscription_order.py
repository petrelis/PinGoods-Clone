# Generated by Django 3.2.8 on 2021-12-08 13:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pay', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscription',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pay.order', unique=True),
        ),
    ]