# Generated by Django 4.2.1 on 2024-04-01 03:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_imagecut_out_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagecut',
            name='out_img',
            field=models.ImageField(blank=True, upload_to='out_images'),
        ),
    ]