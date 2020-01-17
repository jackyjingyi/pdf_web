# Generated by Django 3.0 on 2020-01-14 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dapsa', '0007_auto_20200104_1449'),
    ]

    operations = [
        migrations.AddField(
            model_name='testdoc',
            name='asin',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='asinassign',
            name='assign_status',
            field=models.CharField(choices=[('1', 'assigned'), ('2', 'rejected'), ('3', 'complete')], max_length=25),
        ),
        migrations.AlterField(
            model_name='samplepool',
            name='assign_status',
            field=models.CharField(choices=[('1', 'assigned'), ('2', 'rejected'), ('3', 'waiting'), ('4', 'reviewed'), ('5', 'complete not reviewed')], max_length=25),
        ),
    ]
