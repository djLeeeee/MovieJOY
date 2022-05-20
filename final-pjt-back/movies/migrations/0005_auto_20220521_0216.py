# Generated by Django 3.2.12 on 2022-05-21 02:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0004_movie_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='poster_path',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='movie',
            name='vote_average',
            field=models.FloatField(default=0),
        ),
    ]
