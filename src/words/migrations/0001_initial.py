# Generated by Django 3.0.6 on 2020-05-28 14:16

from django.db import migrations, models

import config.utils


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Word",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(max_length=50, unique=True, verbose_name="name"),
                ),
                (
                    "description",
                    models.TextField(
                        blank=True, default="", verbose_name="description"
                    ),
                ),
                (
                    "audio",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to=config.utils.upload_to_classname,
                        verbose_name="audio",
                    ),
                ),
                (
                    "image",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to=config.utils.upload_to_classname,
                        verbose_name="image",
                    ),
                ),
                (
                    "created",
                    models.DateTimeField(auto_now_add=True, verbose_name="created"),
                ),
                (
                    "modified",
                    models.DateTimeField(auto_now=True, verbose_name="modified"),
                ),
            ],
            options={"verbose_name": "word", "verbose_name_plural": "words",},
        ),
    ]
