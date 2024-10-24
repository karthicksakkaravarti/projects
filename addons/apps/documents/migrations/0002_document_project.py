# Generated by Django 5.0.9 on 2024-10-13 16:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("documents", "0001_initial"),
        ("project", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="document",
            name="project",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="documents",
                to="project.project",
            ),
        ),
    ]