# Generated by Django 3.2.23 on 2023-12-06 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(default='pbkdf2_sha256$260000$0ZP08FoeDOivSkCV1AlB2P$6f952frPvuujcIzlUNjZtVAzfDEGKfXwKHTOxDCY0p8=', max_length=128, verbose_name='password'),
        ),
    ]