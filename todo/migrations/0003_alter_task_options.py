# Generated by Django 4.2 on 2024-04-25 18:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("todo", "0002_rename_created_datetime_task_created_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="task",
            options={"ordering": ["-is_done", "-created"]},
        ),
    ]
