# Generated by Django 4.1.4 on 2022-12-25 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("course", "0002_alter_standard_year"),
    ]

    operations = [
        migrations.AlterField(
            model_name="standard",
            name="year",
            field=models.DateTimeField(
                auto_now_add=True, verbose_name="Année académique"
            ),
        ),
    ]
