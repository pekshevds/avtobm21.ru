# Generated by Django 4.2.7 on 2024-06-07 03:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog_app', '0007_good_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='good',
            name='price',
        ),
    ]
