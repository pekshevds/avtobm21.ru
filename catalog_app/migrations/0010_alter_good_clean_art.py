# Generated by Django 4.2.7 on 2024-06-19 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog_app', '0009_good_clean_art'),
    ]

    operations = [
        migrations.AlterField(
            model_name='good',
            name='clean_art',
            field=models.CharField(blank=True, db_index=True, default='', max_length=50, null=True, verbose_name='Артикул для поиска'),
        ),
    ]
