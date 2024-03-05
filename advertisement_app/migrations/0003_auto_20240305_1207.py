# Generated by Django 3.2.23 on 2024-03-05 09:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('advertisement_app', '0002_groupofproperty_alter_property_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='groupofproperty',
            options={'verbose_name': 'Группа свойств', 'verbose_name_plural': 'Группы свойств объевлений'},
        ),
        migrations.AlterField(
            model_name='valuepropertyofanadvertisement',
            name='advertisement',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='properties', to='advertisement_app.advertisement', verbose_name='Рекламное объявление'),
        ),
    ]
