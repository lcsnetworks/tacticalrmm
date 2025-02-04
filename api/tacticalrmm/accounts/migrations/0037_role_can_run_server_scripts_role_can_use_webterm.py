# Generated by Django 4.2.13 on 2024-06-28 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0036_remove_role_can_ping_agents"),
    ]

    operations = [
        migrations.AddField(
            model_name="role",
            name="can_run_server_scripts",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="role",
            name="can_use_webterm",
            field=models.BooleanField(default=False),
        ),
    ]
