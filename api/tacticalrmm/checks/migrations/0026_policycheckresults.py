# Generated by Django 3.2.12 on 2022-03-20 02:21

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('checks', '0025_auto_20210917_1954'),
    ]

    operations = [
        migrations.CreateModel(
            name='PolicyCheckResults',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('passing', 'Passing'), ('failing', 'Failing'), ('pending', 'Pending')], default='pending', max_length=100)),
                ('more_info', models.TextField(blank=True, null=True)),
                ('last_run', models.DateTimeField(blank=True, null=True)),
                ('fail_count', models.PositiveIntegerField(default=0)),
                ('outage_history', models.JSONField(blank=True, null=True)),
                ('extra_details', models.JSONField(blank=True, null=True)),
                ('timeout', models.PositiveIntegerField(blank=True, null=True)),
                ('stdout', models.TextField(blank=True, null=True)),
                ('stderr', models.TextField(blank=True, null=True)),
                ('retcode', models.IntegerField(blank=True, null=True)),
                ('execution_time', models.CharField(blank=True, max_length=100, null=True)),
                ('history', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(blank=True), blank=True, default=list, null=True, size=None)),
                ('policy_check', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='policycheckresults', to='checks.check')),
            ],
        ),
    ]
