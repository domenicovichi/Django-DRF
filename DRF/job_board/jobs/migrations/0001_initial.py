# Generated by Django 4.2.3 on 2023-08-07 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="JobOffer",
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
                ("company_name", models.CharField(max_length=60)),
                ("company_email", models.EmailField(max_length=254)),
                ("job_title", models.CharField(max_length=70)),
                ("salary", models.PositiveIntegerField()),
                ("city", models.CharField(max_length=50)),
                ("state", models.CharField(max_length=50)),
                ("created_at", models.DateField(auto_now_add=True)),
                ("available", models.BooleanField(default=True)),
            ],
        ),
    ]
