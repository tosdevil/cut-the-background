# Generated by Django 4.2.1 on 2024-04-03 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_remove_imagecut_session'),
    ]

    operations = [
        migrations.AddField(
            model_name='imagecut',
            name='uploader_session',
            field=models.CharField(blank=True, max_length=60),
        ),
    ]
