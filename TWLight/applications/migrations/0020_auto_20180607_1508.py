# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-07 15:08


from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [("applications", "0019_application_account_email")]

    operations = [
        migrations.AlterField(
            model_name="application",
            name="editor",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="applications",
                to="users.Editor",
            ),
        ),
        migrations.AlterField(
            model_name="application",
            name="sent_by",
            field=models.ForeignKey(
                blank=True,
                help_text="The user who sent this application to the partner",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
