# Generated by Django 4.2.7 on 2024-04-19 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0023_alter_user_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(default='pbkdf2_sha256$600000$gJgr738wvT47r90ezs2Jtz$FtqpNOiE3suLr4EOFUHMxP796pJGY42SX5IDwsYotBc=', max_length=128, verbose_name='password'),
        ),
    ]
