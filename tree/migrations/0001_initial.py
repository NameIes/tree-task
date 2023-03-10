# Generated by Django 4.1.7 on 2023-02-28 12:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="TreeMenu",
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
                ("name", models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name="TreeItem",
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
                ("name", models.CharField(max_length=80)),
                (
                    "menu",
                    models.ForeignKey(
                        blank=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="tree_items",
                        to="tree.treemenu",
                    ),
                ),
                (
                    "parent",
                    models.ForeignKey(
                        blank=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="childrens",
                        to="tree.treeitem",
                    ),
                ),
            ],
        ),
    ]
