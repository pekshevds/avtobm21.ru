# Generated by Django 4.2.7 on 2024-06-06 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0028_alter_user_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(default='pbkdf2_sha256$600000$Yi4ZYbBH7KjyybVnwnhpyQ$kKGzisPNfcBabniET9pNQHKgcIoij0bPrjFB+MYWfx8=', max_length=128, verbose_name='password'),
        ),
    ]