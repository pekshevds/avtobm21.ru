# Generated by Django 4.2.7 on 2024-06-07 03:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0032_alter_user_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(default='pbkdf2_sha256$600000$G1r5cN9sdSuQK04YsHphcp$I/VsLE7AknrVxxcOrR6dm/Ue50qtXec0HU2dGYTQXBU=', max_length=128, verbose_name='password'),
        ),
    ]