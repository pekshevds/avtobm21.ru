# Generated by Django 4.2.7 on 2023-12-07 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='good',
            name='art',
            field=models.CharField(blank=True, db_index=True, default='', max_length=50, null=True, verbose_name='Артикул'),
        ),
    ]