from django.db import models
from django.utils import timezone
from .enums import KursmaterialEnum, KorrekturstatusEnum

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

    def __str__(self):
        return f"{self.get_typ_display()} - {self.kurs}"


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
    beschreibung = models.TextField(default="Keine Beschreibung")

    class Meta:
        verbose_name_plural = "Korrekturen"


class Messages(models.Model):
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
    text = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    sender = models.CharField(
        max_length=2, choices=SenderENUM.choices, default=SenderENUM.STUDENT
    )

    class Meta:
        verbose_name_plural = "Messages"

    def __str__(self):
        return f"""Nachricht von {self.student}
            an {self.tutor} für {self.korrektur}"""


# class Fehlermeldung(models.Model):
#     matrikelnummer = models.CharField(max_length=100) #Ersteller
#     vorname = models.CharField(max_length=100)
#     nachname = models.CharField(max_length=100)
#     email = models.EmailField()
#     kursabkuerzung = models.CharField(max_length=100) #Kurs
#     medium = models.CharField(max_length=100) #Kursmaterial
#     fehlerbeschreibung = models.TextField() #Wird in Korrektur übernommen

#     def __str__(self):
#         return self.matrikelnummer
