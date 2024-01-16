# Generated by Django 4.2.7 on 2024-01-10 07:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("database", "0007_alter_korrektur_aktuellerstatus_messages"),
    ]

    operations = [
        migrations.AlterField(
            model_name="messages",
            name="tutor",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="tutor_messages",
                to="database.tutor",
            ),
        ),
    ]