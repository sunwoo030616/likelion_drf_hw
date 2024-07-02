# Generated by Django 5.0.6 on 2024-07-02 04:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("singer", "0002_song"),
    ]

    operations = [
        migrations.AlterField(
            model_name="song",
            name="singer",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="songs",
                to="singer.singer",
            ),
        ),
    ]
