# Generated by Django 3.2.23 on 2024-01-10 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('image_app', '0002_remove_image_url_image_image_image_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(blank=True, default='', upload_to='images/', verbose_name='Файл изображения'),
        ),
    ]