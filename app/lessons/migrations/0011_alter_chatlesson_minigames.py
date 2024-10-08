# Generated by Django 5.0.8 on 2024-09-04 00:20

import wagtail.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("lessons", "0010_chatlesson_minigames"),
    ]

    operations = [
        migrations.AlterField(
            model_name="chatlesson",
            name="minigames",
            field=wagtail.fields.StreamField(
                [("step_order_game", 7)],
                blank=True,
                block_lookup={
                    0: (
                        "wagtail.blocks.CharBlock",
                        (),
                        {"help_text": "Title of the sequence", "required": True},
                    ),
                    1: (
                        "wagtail.blocks.TextBlock",
                        (),
                        {
                            "help_text": "Description of the sequencing task",
                            "required": True,
                        },
                    ),
                    2: (
                        "wagtail.images.blocks.ImageChooserBlock",
                        (),
                        {
                            "help_text": "Main image for the sequencing task",
                            "required": True,
                        },
                    ),
                    3: (
                        "wagtail.blocks.CharBlock",
                        (),
                        {"help_text": "Name of the step", "required": True},
                    ),
                    4: (
                        "wagtail.images.blocks.ImageChooserBlock",
                        (),
                        {"help_text": "Image for the step", "required": True},
                    ),
                    5: (
                        "wagtail.blocks.StructBlock",
                        [[("name", 3), ("image", 4)]],
                        {},
                    ),
                    6: ("wagtail.blocks.ListBlock", (5,), {}),
                    7: (
                        "wagtail.blocks.StructBlock",
                        [
                            [
                                ("title", 0),
                                ("description", 1),
                                ("main_image", 2),
                                ("steps", 6),
                            ]
                        ],
                        {},
                    ),
                },
            ),
        ),
    ]
