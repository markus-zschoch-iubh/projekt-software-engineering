from django.db import models
from django.utils import timezone

from .enums import KursmaterialEnum, KorrekturstatusEnum
from .helper import sende_email_an_studenten

# Create your models here.


class Kurs(models.Model):
    name = models.CharField(max_length=255)
    kurzname = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "Kurse"

    def __str__(self):
        return f"{self.kurzname} - {self.name}"


class Kursmaterial(models.Model):
    typ = models.CharField(max_length=2, choices=KursmaterialEnum.choices)
    kurs = models.ForeignKey(Kurs, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Kursmaterialien"
        unique_together = ["typ", "kurs"]

    def __str__(self):
        return f"{self.get_typ_display()}"


class Student(models.Model):
    martrikelnummer = models.IntegerField(primary_key=True)
    vorname = models.CharField(max_length=255)
    nachname = models.CharField(max_length=255)
    email = models.EmailField()
    password = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "Studenten"

    def __str__(self):
        return f"{self.nachname}, {self.vorname} ({self.martrikelnummer})"


class Tutor(models.Model):
    vorname = models.CharField(max_length=255)
    nachname = models.CharField(max_length=255)
    email = models.EmailField()
    password = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "Tutoren"

    def __str__(self):
        return f"{self.nachname}, {self.vorname}"


class Korrektur(models.Model):
    ersteller = models.ForeignKey(
        Student, null=True, on_delete=models.SET_NULL
    )
    bearbeiter = models.ForeignKey(
        Tutor, on_delete=models.SET_NULL, blank=True, null=True
    )
    kurs = models.ForeignKey(Kurs, null=True, on_delete=models.SET_NULL)
    kursmaterial = models.ForeignKey(
        Kursmaterial, null=True, on_delete=models.SET_NULL
    )
    aktuellerStatus = models.CharField(
        max_length=2,
        choices=KorrekturstatusEnum.choices,
        default=KorrekturstatusEnum.OFFEN,
    )
    beschreibung = models.TextField(
        default="Bitte tragen Sie hier die Beschreibung des Fehlers ein."
    )

    class Meta:
        verbose_name_plural = "Korrekturen"


class Messages(models.Model):
    class AenderungTypENUM(models.TextChoices):
        EROEFFNUNG = "01", "Eröffnung"
        ZUWEISUNG = "02", "Zuweisung"
        STATUS = "03", "Statusänderung"
        NACHRICHT = "04", "Nachricht"

    class SenderENUM(models.TextChoices):
        TUTOR = "01", "Tutor"
        STUDENT = "02", "Student"

    student = models.ForeignKey(
        Student,
        on_delete=models.SET_NULL,
        null=True,
        related_name="student_messages",
    )
    tutor = models.ForeignKey(
        Tutor,
        on_delete=models.SET_NULL,
        related_name="tutor_messages",
        null=True,
        blank=True,
    )
    korrektur = models.ForeignKey(
        Korrektur, on_delete=models.CASCADE, related_name="korrektur_messages"
    )
    text = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    sender = models.CharField(
        max_length=2, choices=SenderENUM.choices, default=SenderENUM.STUDENT
    )
    status = models.CharField(
        max_length=2,
        choices=KorrekturstatusEnum.choices,
        default=KorrekturstatusEnum.OFFEN,
    )
    aenderung_typ = models.CharField(
        max_length=2,
        choices=AenderungTypENUM.choices,
        default=AenderungTypENUM.EROEFFNUNG,
    )

    class Meta:
        verbose_name_plural = "Messages"

    def __str__(self):
        return f"""Nachricht von {self.student}
            an {self.tutor} für {self.korrektur}"""
    
    def save(self):
        if self.sender == "01":
            previous_message = Messages.objects.all().order_by("-created_at")[0]
            sende_email_an_studenten(self, previous_message)
        return super().save()
