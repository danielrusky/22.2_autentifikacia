# Generated by Django 4.2.9 on 2024-01-14 05:35

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("materials", "0002_material_created_at_material_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="material",
            name="date_modified",
            field=models.DateTimeField(auto_now=True, verbose_name="Дата изменения"),
        ),
    ]
