# Generated by Django 4.2.4 on 2024-04-03 15:32

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("user", "0002_application_moderator_organization_address_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="organization",
            name="name",
        ),
    ]
