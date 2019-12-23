# Generated by Django 3.0 on 2019-12-20 02:35

import dapsa.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dapsa', '0002_auto_20191219_1913'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='document',
            name='doc',
        ),
        migrations.AddField(
            model_name='document',
            name='pl',
            field=models.CharField(default='temp', max_length=255),
        ),
        migrations.AddField(
            model_name='document',
            name='upload',
            field=models.FileField(default='temp', upload_to=dapsa.models.pl_dirtory_path),
            preserve_default=False,
        ),
    ]