# Generated by Django 5.1 on 2024-09-26 06:42

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("bnb_app", "0004_alter_booking_status_options_alter_listing_host"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="listing",
            options={"verbose_name_plural": "Properties"},
        ),
    ]