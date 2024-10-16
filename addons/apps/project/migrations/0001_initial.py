# Generated by Django 5.0.9 on 2024-10-10 19:02

import addons.apps.project.models
import django.db.models.deletion
import django_fsm
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Attribute",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255, unique=True)),
                (
                    "data_type",
                    models.CharField(
                        choices=[
                            ("char", "Text"),
                            ("int", "Integer"),
                            ("bool", "Boolean"),
                            ("date", "Date"),
                            ("float", "Float"),
                        ],
                        max_length=10,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Project",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("name", models.CharField(max_length=255, verbose_name="Project Name")),
                (
                    "description",
                    addons.apps.project.models.WYSIWYGTextField(
                        verbose_name="Description"
                    ),
                ),
                ("start_date", models.DateField(verbose_name="Start Date")),
                ("end_date", models.DateField(verbose_name="End Date")),
                (
                    "status",
                    django_fsm.FSMIntegerField(
                        choices=[
                            (1, "Draft"),
                            (2, "In Progress"),
                            (3, "Completed"),
                            (4, "On Hold"),
                            (5, "Cancelled"),
                            (6, "Rejected"),
                        ],
                        default=1,
                        verbose_name="Status",
                    ),
                ),
                (
                    "owner",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Owner",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ProjectAttributeValue",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("value_char", models.CharField(blank=True, max_length=255, null=True)),
                ("value_int", models.IntegerField(blank=True, null=True)),
                ("value_bool", models.BooleanField(blank=True, null=True)),
                ("value_date", models.DateField(blank=True, null=True)),
                ("value_float", models.FloatField(blank=True, null=True)),
                (
                    "attribute",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="project.attribute",
                    ),
                ),
                (
                    "project",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="attribute_values",
                        to="project.project",
                    ),
                ),
            ],
        ),
    ]
