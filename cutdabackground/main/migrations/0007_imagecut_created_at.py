# Generated by Django 4.2.1 on 2024-04-04 13:57

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_imagecut_uploader_session'),
    ]

    operations = [
        migrations.AddField(
            model_name='imagecut',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
