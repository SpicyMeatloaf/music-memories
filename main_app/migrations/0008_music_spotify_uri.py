# Generated by Django 3.2.5 on 2021-07-29 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0007_music_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='music',
            name='spotify_uri',
            field=models.CharField(default=None, max_length=100),
            preserve_default=False,
        ),
    ]