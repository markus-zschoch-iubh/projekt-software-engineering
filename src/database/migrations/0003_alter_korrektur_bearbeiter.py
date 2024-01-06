# Generated by Django 4.2.7 on 2024-01-02 18:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("database", "0002_alter_korrektur_bearbeiter"),
    ]

    operations = [
        migrations.AlterField(
            model_name="korrektur",
            name="bearbeiter",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="database.tutor",
            ),
        ),
    ]