# Generated by Django 5.1 on 2024-10-01 20:05

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("bnb_app", "0008_review"),
        ("users", "0006_alter_bookings_options"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="book_count",
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name="profile",
            name="bookings_made",
            field=models.ManyToManyField(blank=True, to="bnb_app.listing"),
        ),
        migrations.DeleteModel(
            name="Bookings",
        ),
    ]