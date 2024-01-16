# Generated by Django 4.2.7 on 2024-01-13 11:25

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        (
            "webhook",
            "0002_korrektur_kurs_student_tutor_video_podcast_pdfskript_and_more",
        ),
    ]

    operations = [
        migrations.RemoveField(
            model_name="allgemeinsonstiges",
            name="korrektur",
        ),
        migrations.DeleteModel(
            name="Fehlermeldung",
        ),
        migrations.RemoveField(
            model_name="gedrucktesskript",
            name="korrektur",
        ),
        migrations.RemoveField(
            model_name="iulearnandroid",
            name="korrektur",
        ),
        migrations.RemoveField(
            model_name="iulearniphone",
            name="korrektur",
        ),
        migrations.RemoveField(
            model_name="iulearnweb",
            name="korrektur",
        ),
        migrations.RemoveField(
            model_name="korrektur",
            name="bearbeiter",
        ),
        migrations.RemoveField(
            model_name="korrektur",
            name="ersteller",
        ),
        migrations.RemoveField(
            model_name="korrektur",
            name="kurs",
        ),
        migrations.RemoveField(
            model_name="kursmaterial",
            name="kurs",
        ),
        migrations.RemoveField(
            model_name="pdfskript",
            name="korrektur",
        ),
        migrations.RemoveField(
            model_name="podcast",
            name="korrektur",
        ),
        migrations.RemoveField(
            model_name="video",
            name="korrektur",
        ),
        migrations.DeleteModel(
            name="AllgemeinSonstiges",
        ),
        migrations.DeleteModel(
            name="GedrucktesSkript",
        ),
        migrations.DeleteModel(
            name="IULearnAndroid",
        ),
        migrations.DeleteModel(
            name="IULearnIPhone",
        ),
        migrations.DeleteModel(
            name="IULearnWeb",
        ),
        migrations.DeleteModel(
            name="Korrektur",
        ),
        migrations.DeleteModel(
            name="Kurs",
        ),
        migrations.DeleteModel(
            name="Kursmaterial",
        ),
        migrations.DeleteModel(
            name="PDFSkript",
        ),
        migrations.DeleteModel(
            name="Podcast",
        ),
        migrations.DeleteModel(
            name="Student",
        ),
        migrations.DeleteModel(
            name="Tutor",
        ),
        migrations.DeleteModel(
            name="Video",
        ),
    ]
