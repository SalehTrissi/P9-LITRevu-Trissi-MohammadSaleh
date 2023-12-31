# Generated by Django 4.2.3 on 2023-07-29 15:56

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0003_alter_review_body_alter_review_headline"),
    ]

    operations = [
        migrations.AlterField(
            model_name="review",
            name="rating",
            field=models.PositiveSmallIntegerField(
                choices=[(0, "0"), (1, "1"), (2, "2"), (3, "3"), (4, "4"), (5, "5")],
                default=0,
                validators=[
                    django.core.validators.MinValueValidator(0),
                    django.core.validators.MaxValueValidator(5),
                ],
                verbose_name="Note",
            ),
        ),
        migrations.AlterField(
            model_name="ticket",
            name="image",
            field=models.ImageField(
                blank=True, null=True, upload_to="images/", verbose_name="Image"
            ),
        ),
    ]
