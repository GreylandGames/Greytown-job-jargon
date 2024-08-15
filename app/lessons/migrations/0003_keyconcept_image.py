# Generated by Django 5.0.8 on 2024-08-15 05:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("lessons", "0002_lesson_language"),
        ("wagtailimages", "0026_delete_uploadedimage"),
    ]

    operations = [
        migrations.AddField(
            model_name="keyconcept",
            name="image",
            field=models.ForeignKey(
                blank=True,
                help_text="Choose an image that represents the key concept. This will help the student visualize the concept.",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="wagtailimages.image",
            ),
        ),
    ]
