# Generated for the AWP Django portfolio project.

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="GeneralSetting",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("updated_date", models.DateTimeField(auto_now=True, verbose_name="Updated Date")),
                ("created_date", models.DateTimeField(auto_now_add=True, verbose_name="Created Date")),
                ("name", models.CharField(blank=True, default="", help_text="This is variable of the setting.", max_length=254, verbose_name="Name")),
                ("description", models.CharField(blank=True, default="", max_length=254, verbose_name="Description")),
                ("parameter", models.CharField(blank=True, default="", max_length=254, verbose_name="Parameter")),
            ],
            options={
                "verbose_name": "General Setting",
                "verbose_name_plural": "General Settings",
                "ordering": ("name",),
            },
        ),
    ]
