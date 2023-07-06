# Generated by Django 4.2.3 on 2023-07-05 15:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("db", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="CinemaHall",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=255)),
                ("rows", models.IntegerField()),
                ("seats_in_row", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="Movie",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("title", models.CharField(max_length=255)),
                ("description", models.TextField()),
                ("actors", models.ManyToManyField(related_name="actors", to="db.actor")),
                ("genres", models.ManyToManyField(related_name="genres", to="db.genre")),
            ],
        ),
        migrations.CreateModel(
            name="MovieSession",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("show_time", models.DateTimeField()),
                ("cinema_hall", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="db.cinemahall")),
                ("movie", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="db.movie")),
            ],
        ),
    ]