# Generated by Django 4.2.3 on 2023-08-11 11:21

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0002_alter_menuitem_parent"),
    ]

    operations = [
        migrations.CreateModel(
            name="FooterItem",
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
                ("title", models.CharField(max_length=255)),
                (
                    "link",
                    models.CharField(
                        blank=True, default="#", max_length=255, null=True
                    ),
                ),
            ],
        ),
    ]
