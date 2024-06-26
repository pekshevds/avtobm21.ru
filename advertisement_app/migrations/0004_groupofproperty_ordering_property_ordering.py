# Generated by Django 4.2.7 on 2024-04-08 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advertisement_app', '0003_auto_20240305_1207'),
    ]

    operations = [
        migrations.AddField(
            model_name='groupofproperty',
            name='ordering',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=4, null=True, verbose_name='Опрядок сортировки'),
        ),
        migrations.AddField(
            model_name='property',
            name='ordering',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=4, null=True, verbose_name='Опрядок сортировки'),
        ),
    ]
