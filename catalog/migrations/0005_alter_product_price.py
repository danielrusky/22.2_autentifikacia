# Generated by Django 4.2.9 on 2024-01-14 10:24

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("catalog", "0004_version"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="price",
            field=models.PositiveIntegerField(default=0, verbose_name="Цена"),
        ),
    ]