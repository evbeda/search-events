# Generated by Django 3.0.5 on 2020-06-01 20:46

from django.db import migrations, models
import django.db.models.deletion
import search_events_app.mixins.get_context_mixin


class Migration(migrations.Migration):

    dependencies = [
        ('search_events_app', '0011_populate_currency'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('code', models.CharField(max_length=2)),
                ('country', models.CharField(max_length=2)),
            ],
            options={
                'verbose_name_plural': 'Cities',
            },
            bases=(models.Model, search_events_app.mixins.get_context_mixin.GetContextMixin),
        ),
    ]