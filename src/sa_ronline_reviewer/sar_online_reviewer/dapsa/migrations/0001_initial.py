# Generated by Django 3.0 on 2020-01-02 13:30

import dapsa.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ExtractionLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='MappingLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='SamplePool',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parent_asin', models.CharField(max_length=50)),
                ('region_id', models.IntegerField()),
                ('marketplace_id', models.IntegerField()),
                ('asin', models.CharField(max_length=50)),
                ('ifdone', models.CharField(default='fresh', max_length=25)),
                ('brand_code', models.CharField(blank=True, max_length=25, null=True)),
                ('item_name', models.TextField(blank=True, null=True)),
                ('style', models.CharField(blank=True, max_length=25, null=True)),
                ('risk_level', models.IntegerField(blank=True, null=True)),
                ('classification_type', models.CharField(blank=True, max_length=50, null=True)),
                ('product_type', models.CharField(blank=True, max_length=100, null=True)),
                ('brand_name', models.CharField(blank=True, max_length=100, null=True)),
                ('product_group_description', models.CharField(blank=True, max_length=100, null=True)),
                ('parent_asin_name', models.TextField(blank=True, null=True)),
                ('edition', models.CharField(max_length=25)),
                ('max_available_quantity', models.IntegerField(blank=True, null=True)),
                ('min_available_quantity', models.IntegerField(blank=True, null=True)),
                ('eod_available_quantity', models.IntegerField(blank=True, null=True)),
                ('all_vendors', models.TextField(blank=True, null=True)),
                ('first_vendor', models.CharField(blank=True, max_length=25, null=True)),
                ('vendor_name', models.TextField(blank=True, null=True)),
                ('sub_parent_asin_number', models.IntegerField(blank=True, null=True)),
                ('ifpick', models.CharField(default='not pick', max_length=25)),
                ('assign_date', models.DateTimeField(blank=True, null=True)),
                ('assign_status', models.CharField(choices=[('1', 'assigned'), ('2', 'rejected'), ('3', 'waiting')], max_length=25)),
                ('assignee', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TestDoc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caseid', models.CharField(max_length=255)),
                ('pl', models.CharField(max_length=255)),
                ('docfile', models.FileField(upload_to=dapsa.models.pl_dirtory_path)),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('uploaded_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, to_field='username')),
            ],
        ),
        migrations.CreateModel(
            name='Protocols',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caseid', models.CharField(blank=True, max_length=255, null=True)),
                ('protocol_name', models.CharField(max_length=200, unique=True, verbose_name='Protocol Name')),
                ('short_cut', models.CharField(blank=True, max_length=50, null=True)),
                ('version', models.CharField(blank=True, max_length=25, null=True)),
                ('amazon_number', models.IntegerField(blank=True, null=True)),
                ('uploaded_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('uploaded_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Protocol',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('speck_number', models.CharField(blank=True, max_length=30, null=True, verbose_name='Speck Number')),
                ('regulation', models.TextField(blank=True, null=True, verbose_name='Regulation')),
                ('requirement_title', models.TextField(blank=True, null=True, verbose_name='Requirement title')),
                ('link', models.URLField(blank=True, null=True)),
                ('region', models.CharField(blank=True, max_length=100, null=True, verbose_name='Region')),
                ('test_method', models.TextField(blank=True, null=True, verbose_name='Test Method')),
                ('requirement', models.TextField(blank=True, null=True, verbose_name='Requirement')),
                ('protduct_scope', models.CharField(blank=True, max_length=100, verbose_name='Product Scope')),
                ('exemption', models.CharField(blank=True, default='NA', max_length=30)),
                ('protocol_section', models.CharField(blank=True, max_length=100, null=True)),
                ('mandatory_voluntary', models.CharField(blank=True, max_length=30, null=True)),
                ('is_cornerstone', models.BooleanField(default=False, verbose_name='Is Cornerstone')),
                ('new_voluntary_safety_standard', models.TextField(blank=True, null=True, verbose_name='New Voluntary Safety Standard')),
                ('reationale', models.CharField(blank=True, max_length=50, null=True, verbose_name='Reationale')),
                ('upload_date', models.DateTimeField(auto_now_add=True)),
                ('latest_update_date', models.DateTimeField(auto_now=True)),
                ('last_updated_by_1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='last_updated', to=settings.AUTH_USER_MODEL)),
                ('protocol_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dapsa.Protocols', to_field='protocol_name')),
                ('uploaded_by_1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='uploaded', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='MiningQueue',
            fields=[
                ('sessionid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('caseid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dapsa.TestDoc')),
            ],
        ),
        migrations.CreateModel(
            name='MiningLog',
            fields=[
                ('caseid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('start_time', models.DateTimeField(auto_now_add=True)),
                ('stage1', models.CharField(choices=[('1', 'Processing'), ('2', 'Success'), ('3', 'Fail'), ('4', 'Stop')], max_length=3)),
                ('stage2', models.CharField(choices=[('1', 'Processing'), ('2', 'Success'), ('3', 'Fail'), ('4', 'Stop')], max_length=3)),
                ('end_time', models.DateTimeField(auto_now=True)),
                ('doc_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='dapsa.TestDoc')),
            ],
        ),
        migrations.CreateModel(
            name='ConlusionInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('frequence', models.IntegerField(default=0)),
                ('phased_requirement_title', models.CharField(max_length=200)),
                ('scenario', models.CharField(choices=[('1', 'Missing'), ('2', 'Pass'), ('3', 'Fail')], max_length=3)),
                ('page', models.IntegerField(default=0)),
                ('reasons', models.TextField()),
                ('comments', models.TextField()),
                ('caseid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dapsa.MiningLog')),
                ('protocol_section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='protocol_section_r', to='dapsa.Protocol')),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='region_r', to='dapsa.Protocol')),
                ('requirement_title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='requirement_title_r', to='dapsa.Protocol')),
            ],
        ),
        migrations.CreateModel(
            name='BasicInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('asin', models.CharField(max_length=50)),
                ('protocol', models.CharField(max_length=200)),
                ('extract_report_date', models.CharField(max_length=100)),
                ('vendor', models.CharField(max_length=200)),
                ('factory', models.CharField(max_length=200)),
                ('caseid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dapsa.MiningLog')),
            ],
        ),
        migrations.CreateModel(
            name='AsinAssign',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assign_date', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('assign_status', models.CharField(choices=[('1', 'assigned'), ('2', 'rejected')], max_length=25)),
                ('asin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dapsa.SamplePool')),
                ('assignee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
