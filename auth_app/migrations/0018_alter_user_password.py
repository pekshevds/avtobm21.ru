# Generated by Django 4.2.7 on 2024-03-09 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0017_alter_user_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(default='pbkdf2_sha256$600000$vlCwDRKXX4V8vp985Xmnui$ls+brFbOwPFF+bpdBQ2xq7OWCeyKoS56If6USXKJdss=', max_length=128, verbose_name='password'),
        ),
    ]
