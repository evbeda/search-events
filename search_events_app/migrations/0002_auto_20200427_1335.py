# Generated by Django 3.0.5 on 2020-04-27 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search_events_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='country',
            name='flag',
            field=models.URLField(),
        ),
    ]
