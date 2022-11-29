# Generated by Django 4.1.2 on 2022-11-28 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("scanpipe", "0026_run_current_step"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="webhooksubscription",
            name="sent",
        ),
        migrations.AddField(
            model_name="webhooksubscription",
            name="delivery_error",
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name="webhooksubscription",
            name="response_status_code",
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="webhooksubscription",
            name="response_text",
            field=models.TextField(blank=True),
        ),
    ]
