# Generated by Django 3.2.5 on 2021-07-29 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0012_alter_music_spotify_uri'),
    ]

    operations = [
        migrations.AlterField(
            model_name='music',
            name='spotify_uri',
            field=models.CharField(blank=True, default=' ', max_length=100),
        ),
    ]