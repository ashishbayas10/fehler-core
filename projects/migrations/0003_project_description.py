# Generated by Django 2.2.26 on 2022-02-02 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("projects", "0002_auto_20220124_1503"),
    ]

    operations = [
        migrations.AddField(
            model_name="project",
            name="description",
            field=models.TextField(blank=True, null=True),
        ),
    ]
