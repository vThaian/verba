# Generated by Django 3.0.6 on 2020-05-28 14:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("words", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Sentence",
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
                ("name", models.CharField(max_length=200, verbose_name="name")),
                (
                    "word",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="sentences",
                        to="words.Word",
                    ),
                ),
            ],
            options={"verbose_name": "sentence", "verbose_name_plural": "sentences",},
        ),
    ]
