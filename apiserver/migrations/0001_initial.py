# Generated by Django 4.1.3 on 2022-11-16 05:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="SeoulGu",
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
                ("name", models.CharField(max_length=10)),
                ("drain_gu_code", models.CharField(max_length=3)),
                ("rain_gu_code", models.CharField(blank=True, max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name="RainLocation",
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
                ("location_info", models.CharField(max_length=200)),
                ("location_code", models.CharField(max_length=4)),
                (
                    "gu",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="apiserver.seoulgu",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="DrainLocation",
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
                ("location_info", models.CharField(max_length=200)),
                ("location_code", models.CharField(max_length=7)),
                (
                    "gu",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="apiserver.seoulgu",
                    ),
                ),
            ],
        ),
    ]
