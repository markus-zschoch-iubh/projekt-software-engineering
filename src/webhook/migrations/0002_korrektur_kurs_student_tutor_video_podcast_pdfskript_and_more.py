# Generated by Django 4.2.7 on 2024-01-04 19:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("webhook", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Korrektur",
            fields=[
                ("id", models.IntegerField(primary_key=True, serialize=False)),
                (
                    "typ",
                    models.CharField(
                        choices=[
                            ("01", "Gedrucktes Skript"),
                            ("02", "PDF Skript"),
                            ("03", "IU Learn (Web)"),
                            ("04", "IU Learn (iPhone)"),
                            ("05", "IU Learn (Android)"),
                            ("06", "Podcast"),
                            ("07", "Video"),
                            ("08", "Sonstiges/Allgemein"),
                        ],
                        max_length=2,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Kurs",
            fields=[
                ("id", models.IntegerField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=255)),
                ("kurzname", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="Student",
            fields=[
                (
                    "martrikelnummer",
                    models.IntegerField(primary_key=True, serialize=False),
                ),
                ("vorname", models.CharField(max_length=255)),
                ("nachname", models.CharField(max_length=255)),
                ("email", models.EmailField(max_length=254)),
                ("password", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="Tutor",
            fields=[
                ("id", models.IntegerField(primary_key=True, serialize=False)),
                ("vorname", models.CharField(max_length=255)),
                ("nachname", models.CharField(max_length=255)),
                ("email", models.EmailField(max_length=254)),
                ("password", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="Video",
            fields=[
                ("id", models.IntegerField(primary_key=True, serialize=False)),
                ("episode", models.CharField(max_length=255)),
                ("zeit", models.CharField(max_length=255)),
                ("beschreibung", models.TextField()),
                (
                    "korrektur",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="webhook.korrektur",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Podcast",
            fields=[
                ("id", models.IntegerField(primary_key=True, serialize=False)),
                ("episode", models.CharField(max_length=255)),
                ("beschreibung", models.TextField()),
                (
                    "korrektur",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="webhook.korrektur",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="PDFSkript",
            fields=[
                ("id", models.IntegerField(primary_key=True, serialize=False)),
                ("seite", models.CharField(max_length=255)),
                ("beschreibung", models.TextField()),
                (
                    "korrektur",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="webhook.korrektur",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Kursmaterial",
            fields=[
                ("id", models.IntegerField(primary_key=True, serialize=False)),
                (
                    "typ",
                    models.CharField(
                        choices=[
                            ("01", "Gedrucktes Skript"),
                            ("02", "PDF Skript"),
                            ("03", "IU Learn (Web)"),
                            ("04", "IU Learn (iPhone)"),
                            ("05", "IU Learn (Android)"),
                            ("06", "Podcast"),
                            ("07", "Video"),
                            ("08", "Sonstiges/Allgemein"),
                        ],
                        max_length=2,
                    ),
                ),
                (
                    "kurs",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="webhook.kurs",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="korrektur",
            name="bearbeiter",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="webhook.tutor"
            ),
        ),
        migrations.AddField(
            model_name="korrektur",
            name="ersteller",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="webhook.student",
            ),
        ),
        migrations.AddField(
            model_name="korrektur",
            name="kurs",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="webhook.kurs"
            ),
        ),
        migrations.CreateModel(
            name="IULearnWeb",
            fields=[
                ("id", models.IntegerField(primary_key=True, serialize=False)),
                ("kapitel", models.CharField(max_length=255)),
                ("unterkapitel", models.CharField(max_length=255, null=True)),
                ("beschreibung", models.TextField()),
                (
                    "korrektur",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="webhook.korrektur",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="IULearnIPhone",
            fields=[
                ("id", models.IntegerField(primary_key=True, serialize=False)),
                ("kapitel", models.CharField(max_length=255)),
                ("unterkapitel", models.CharField(max_length=255, null=True)),
                ("beschreibung", models.TextField()),
                (
                    "korrektur",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="webhook.korrektur",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="IULearnAndroid",
            fields=[
                ("id", models.IntegerField(primary_key=True, serialize=False)),
                ("kapitel", models.CharField(max_length=255)),
                ("unterkapitel", models.CharField(max_length=255, null=True)),
                ("beschreibung", models.TextField()),
                (
                    "korrektur",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="webhook.korrektur",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="GedrucktesSkript",
            fields=[
                ("id", models.IntegerField(primary_key=True, serialize=False)),
                ("seite", models.CharField(max_length=255)),
                ("beschreibung", models.TextField()),
                (
                    "korrektur",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="webhook.korrektur",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="AllgemeinSonstiges",
            fields=[
                ("id", models.IntegerField(primary_key=True, serialize=False)),
                ("beschreibung", models.TextField()),
                (
                    "korrektur",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="webhook.korrektur",
                    ),
                ),
            ],
        ),
    ]
