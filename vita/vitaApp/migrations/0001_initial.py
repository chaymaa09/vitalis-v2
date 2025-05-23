# Generated by Django 5.2 on 2025-04-22 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="User",
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
                ("FirstName", models.CharField(max_length=50)),
                ("LastName", models.CharField(max_length=50)),
                (
                    "Gender",
                    models.CharField(
                        choices=[("Male", "Male"), ("Female", "Female")], max_length=50
                    ),
                ),
                ("BirthDate", models.DateField()),
                ("weight", models.FloatField(help_text="Weight in Kg")),
                ("height", models.FloatField(help_text="Height in Cm")),
            ],
        ),
    ]
