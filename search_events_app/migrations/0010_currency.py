# Generated by Django 3.0.5 on 2020-06-01 18:14

from django.db import migrations, models
import search_events_app.mixins.get_context_mixin


class Migration(migrations.Migration):

    dependencies = [
        ('search_events_app', '0009_populate_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('code', models.CharField(max_length=3)),
            ],
            options={
                'verbose_name_plural': 'Currencies',
            },
            bases=(models.Model, search_events_app.mixins.get_context_mixin.GetContextMixin),
        ),
    ]
