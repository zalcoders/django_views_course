# Generated by Django 5.1.5 on 2025-02-25 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('gamer_tag', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('subject', models.CharField(max_length=50)),
                ('attachment', models.FileField(blank=True, null=True, upload_to='')),
                ('message', models.TextField()),
            ],
        ),
    ]
