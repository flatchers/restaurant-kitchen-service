# Generated by Django 5.0 on 2023-12-15 10:13

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("kitchen", "0002_alter_cook_year_of_experience"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="cook",
            options={"ordering": ["year_of_experience"]},
        ),
    ]
