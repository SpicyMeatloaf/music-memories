# Generated by Django 3.2.5 on 2021-07-20 02:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='music',
            name='date_created',
            field=models.DateField(),
        ),
    ]