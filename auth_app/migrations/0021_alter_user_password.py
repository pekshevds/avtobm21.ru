# Generated by Django 4.2.7 on 2024-03-09 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0020_alter_user_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(default='pbkdf2_sha256$600000$BMLIe7pz5BXtrIuMYpeF1z$+h3Wl5USE83Cmvem5nwEAiIDFSJjB94SaSdE4cH5c/Y=', max_length=128, verbose_name='password'),
        ),
    ]
