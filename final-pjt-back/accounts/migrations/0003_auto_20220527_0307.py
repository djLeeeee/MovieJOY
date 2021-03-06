# Generated by Django 3.2.12 on 2022-05-27 03:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20220526_0017'),
    ]

    operations = [
        migrations.AddField(
            model_name='sms_auth',
            name='time_stamp',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='sms_auth',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='smsauth', to='accounts.user'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='phone_number',
            field=models.CharField(default=0, max_length=11),
        ),
    ]
