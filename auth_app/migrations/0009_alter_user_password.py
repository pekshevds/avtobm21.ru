# Generated by Django 3.2.23 on 2024-01-10 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0008_alter_user_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(default='pbkdf2_sha256$260000$tY1RiZpxn47iPBYifP1f3T$0FNNAJ577/ABawMyRBRgNC3/JNFkTIZSAiknEg1Ajfg=', max_length=128, verbose_name='password'),
        ),
    ]
