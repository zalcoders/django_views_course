# Generated by Django 5.1.5 on 2025-02-07 09:14

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortner', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shortenedurl',
            name='slug',
            field=models.SlugField(blank=True, default=uuid.uuid4, max_length=32, unique=True),
        ),
    ]
