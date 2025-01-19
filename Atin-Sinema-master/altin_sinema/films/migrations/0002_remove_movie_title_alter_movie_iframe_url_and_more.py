# Generated by Django 5.1 on 2024-10-20 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='title',
        ),
        migrations.AlterField(
            model_name='movie',
            name='iframe_url',
            field=models.URLField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='movie',
            name='image_url',
            field=models.URLField(max_length=1000),
        ),
    ]
