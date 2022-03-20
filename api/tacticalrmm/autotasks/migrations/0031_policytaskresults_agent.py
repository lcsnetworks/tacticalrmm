# Generated by Django 3.2.12 on 2022-03-20 02:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('agents', '0046_alter_agenthistory_command'),
        ('autotasks', '0030_auto_20220320_0221'),
    ]

    operations = [
        migrations.AddField(
            model_name='policytaskresults',
            name='agent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='policytaskhistory', to='agents.agent'),
        ),
    ]
