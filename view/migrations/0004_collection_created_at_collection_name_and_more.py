# Generated by Django 5.0.4 on 2024-04-14 10:07

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('view', '0003_collection_places_delete_pov'),
    ]

    operations = [
        migrations.AddField(
            model_name='collection',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='collection',
            name='name',
            field=models.CharField(default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='places',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default='timezone.now'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='places',
            name='name',
            field=models.CharField(default='timezone', max_length=50),
            preserve_default=False,
        ),
    ]
