# Generated by Django 4.1.7 on 2023-02-28 13:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("tree", "0002_alter_treeitem_menu_alter_treeitem_parent"),
    ]

    operations = [
        migrations.AlterField(
            model_name="treeitem",
            name="menu",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="childrens",
                to="tree.treemenu",
            ),
        ),
    ]
