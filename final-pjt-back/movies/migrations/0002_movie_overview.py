# Generated by Django 3.2.12 on 2022-05-23 23:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='overview',
            field=models.CharField(default=1, max_length=500),
            preserve_default=False,
        ),
    ]
