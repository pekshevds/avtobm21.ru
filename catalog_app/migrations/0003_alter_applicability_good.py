# Generated by Django 4.2.7 on 2024-04-08 05:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog_app', '0002_alter_good_art'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicability',
            name='good',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='applicabilities', to='catalog_app.good', verbose_name='Номенклатура'),
        ),
    ]