# Generated by Django 3.2.5 on 2021-07-17 22:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Music',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateField(verbose_name='date created')),
                ('artist', models.CharField(max_length=100)),
                ('album', models.CharField(max_length=100)),
                ('song', models.CharField(max_length=100)),
                ('genre', models.CharField(max_length=100)),
                ('comments', models.CharField(max_length=1000)),
            ],
        ),
    ]
