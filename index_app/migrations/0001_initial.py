# Generated by Django 4.2.7 on 2024-06-06 10:31

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('price_app', '0004_alter_price_index_together_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Const',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('comment', models.TextField(blank=True, null=True, verbose_name='Комментарий')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Дата изменения')),
                ('kind_price', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='price_app.kindprice', verbose_name='Вид цен')),
            ],
            options={
                'verbose_name': 'Константы',
                'verbose_name_plural': 'Константы',
                'ordering': ['-created_at'],
            },
        ),
    ]
