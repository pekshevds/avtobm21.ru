# Generated by Django 4.2.7 on 2024-03-09 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order_app', '0006_alter_orderstatus_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderstatus',
            name='value',
            field=models.CharField(blank=True, db_index=True, max_length=2, null=True, verbose_name='Значение'),
        ),
    ]
