# Generated by Django 4.2.7 on 2024-03-09 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0019_alter_user_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(default='pbkdf2_sha256$600000$T3CmHXm7E1IbRIsvaTii6w$3I3fjDRK6hhu6E0LjKFMHUWg9D8BQEOGJXdIgm3/edY=', max_length=128, verbose_name='password'),
        ),
    ]