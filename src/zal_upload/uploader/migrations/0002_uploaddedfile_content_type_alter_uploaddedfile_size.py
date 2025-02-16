# Generated by Django 5.1.5 on 2025-02-16 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uploader', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='uploaddedfile',
            name='content_type',
            field=models.CharField(default='', max_length=50, verbose_name='Content Type'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='uploaddedfile',
            name='size',
            field=models.FloatField(verbose_name='File Size'),
        ),
    ]
