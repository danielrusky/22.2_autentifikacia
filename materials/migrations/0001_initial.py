# Generated by Django 4.2.9 on 2024-01-13 13:44

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Material",
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
                ("title", models.CharField(max_length=100, verbose_name="название")),
                ("body", models.TextField(verbose_name="содержимое")),
                (
                    "views_count",
                    models.IntegerField(default=0, verbose_name="Просмотры"),
                ),
                (
                    "is_published",
                    models.BooleanField(default=True, verbose_name="Опубликовано"),
                ),
                (
                    "slug",
                    models.CharField(
                        blank=True, max_length=150, null=True, verbose_name="slug"
                    ),
                ),
            ],
            options={
                "verbose_name": "материал",
                "verbose_name_plural": "материалы",
            },
        ),
    ]
