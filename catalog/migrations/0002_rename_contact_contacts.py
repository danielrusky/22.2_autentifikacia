# Generated by Django 4.2.9 on 2024-01-28 08:25

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("catalog", "0001_initial"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Contact",
            new_name="Contacts",
        ),
    ]