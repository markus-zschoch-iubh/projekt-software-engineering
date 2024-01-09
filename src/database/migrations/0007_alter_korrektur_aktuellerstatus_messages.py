# Generated by Django 4.2.7 on 2024-01-09 19:30

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        ("database", "0006_remove_korrektur_kursmaterial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="korrektur",
            name="aktuellerStatus",
            field=models.CharField(
                choices=[
                    ("01", "Offen"),
                    ("02", "In Bearbeitung"),
                    ("03", "Umgesetzt"),
                    ("04", "Abgelehnt"),
                ],
                default="01",
                max_length=2,
            ),
        ),
        migrations.CreateModel(
            name="Messages",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("text", models.TextField()),
                (
                    "created_at",
                    models.DateTimeField(default=django.utils.timezone.now),
                ),
                ("is_read", models.BooleanField(default=False)),
                (
                    "korrektur",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="korrektur_messages",
                        to="database.korrektur",
                    ),
                ),
                (
                    "student",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="student_messages",
                        to="database.student",
                    ),
                ),
                (
                    "tutor",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="tutor_messages",
                        to="database.tutor",
                    ),
                ),
            ],
        ),
    ]
