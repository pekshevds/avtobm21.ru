# Generated by Django 4.2.7 on 2024-03-09 06:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order_app', '0005_alter_orderstatus_value'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='orderstatus',
            options={'verbose_name': 'Статус заказ покупателя', 'verbose_name_plural': 'Статусы заказов покупателей'},
        ),
    ]