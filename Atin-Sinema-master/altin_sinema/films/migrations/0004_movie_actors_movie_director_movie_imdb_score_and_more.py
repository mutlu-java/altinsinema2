# Generated by Django 5.1 on 2024-10-22 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0003_movie_title_alter_movie_iframe_url_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='actors',
            field=models.TextField(default='Unknown Actors'),
        ),
        migrations.AddField(
            model_name='movie',
            name='director',
            field=models.CharField(default='Unknown Director', max_length=100),
        ),
        migrations.AddField(
            model_name='movie',
            name='imdb_score',
            field=models.DecimalField(decimal_places=1, default=0.0, max_digits=3),
        ),
        migrations.AddField(
            model_name='movie',
            name='release_year',
            field=models.IntegerField(default=2000),
        ),
        migrations.AlterField(
            model_name='movie',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]
