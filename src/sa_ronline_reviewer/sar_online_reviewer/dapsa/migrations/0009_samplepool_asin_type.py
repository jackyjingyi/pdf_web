# Generated by Django 3.0 on 2020-01-16 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dapsa', '0008_auto_20200114_1701'),
    ]

    operations = [
        migrations.AddField(
            model_name='samplepool',
            name='asin_type',
            field=models.CharField(blank=True, choices=[('1', 'SPB'), ('2', 'HPB'), ('3', 'CPB')], max_length=25, null=True),
        ),
    ]
