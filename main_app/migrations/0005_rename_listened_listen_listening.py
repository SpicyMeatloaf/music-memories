# Generated by Django 3.2.5 on 2021-07-21 02:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_listen'),
    ]

    operations = [
        migrations.RenameField(
            model_name='listen',
            old_name='listened',
            new_name='listening',
        ),
    ]
