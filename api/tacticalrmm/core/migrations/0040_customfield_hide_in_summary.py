# Generated by Django 4.2.9 on 2024-01-28 02:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0039_coresettings_smtp_from_name"),
    ]

    operations = [
        migrations.AddField(
            model_name="customfield",
            name="hide_in_summary",
            field=models.BooleanField(default=False),
        ),
    ]
