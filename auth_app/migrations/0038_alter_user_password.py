# Generated by Django 4.2.7 on 2024-06-12 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0037_alter_user_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(default='pbkdf2_sha256$600000$3u6TyQSsfHzvo0DXORXHx7$8UjH2/Kl7OkDqy13Sp82M3Vu555InfAI3W6a3XDSPxk=', max_length=128, verbose_name='password'),
        ),
    ]
