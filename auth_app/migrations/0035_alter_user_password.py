# Generated by Django 3.2.23 on 2024-06-07 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0034_alter_user_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(default='pbkdf2_sha256$260000$T3AlqNqL1AyusKiypjr86N$VQPt1Qs3p9ve93HY+rLxoG/qAO+QEVqRsdnu980aMjg=', max_length=128, verbose_name='password'),
        ),
    ]
