# Generated by Django 4.2.7 on 2023-12-06 07:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('catalog_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.DecimalField(blank=True, decimal_places=3, default=1, max_digits=15, null=True, verbose_name='Количество')),
                ('good', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='catalog_app.good', verbose_name='Номенклатура')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='cart_items', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Строка корзины',
                'verbose_name_plural': 'Корзина',
            },
        ),
    ]
