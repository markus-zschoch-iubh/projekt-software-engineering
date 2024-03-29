from django.db import models
from django.utils import timezone

from .enums import KursmaterialEnum, KorrekturstatusEnum

# Create your models here.


class Kurs(models.Model):
    """
    Represents a course in the database.
    """

    name = models.CharField(max_length=255)
    kurzname = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "Kurse"

    def __str__(self):
        return f"{self.kurzname} - {self.name}"


class Kursmaterial(models.Model):
    """
    Represents a piece of course material associated with a specific course.
    """

    typ = models.CharField(max_length=2, choices=KursmaterialEnum.choices)
    kurs = models.ForeignKey(Kurs, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Kursmaterialien"
        unique_together = ["typ", "kurs"]

    def __str__(self):
        return f"{self.get_typ_display()}"


class Student(models.Model):
    """
    Represents a student in the database.
    """

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
    """
    Represents a tutor in the system.
    """

    vorname = models.CharField(max_length=255)
    nachname = models.CharField(max_length=255)
    email = models.EmailField()
    password = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "Tutoren"

    def __str__(self):
        return f"{self.nachname}, {self.vorname}"


class Korrektur(models.Model):
    """
    Represents a correction in the system.

    Attributes:
        ersteller (ForeignKey): The student who created the correction.
        bearbeiter (ForeignKey): The tutor assigned to work on the correction.
        kurs (ForeignKey): The course associated with the correction.
        kursmaterial (ForeignKey): The course material related to the
        correction. aktuellerStatus (CharField): The current status of
        the correction. beschreibung (TextField): The description of the error.

    Meta:
        verbose_name_plural (str): The plural name for the model.
    """

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
    """
    Represents a message in the system.

    Attributes:
        AenderungTypENUM (Enum): Enumeration class representing different
        types of changes.
        SenderENUM (Enum): Enumeration class for sender types.
        student (ForeignKey): ForeignKey to the Student model.
        tutor (ForeignKey): ForeignKey to the Tutor model.
        korrektur (ForeignKey): ForeignKey to the Korrektur model.
        text (TextField): Text field for the message content.
        created_at (DateTimeField): DateTimeField for the creation timestamp.
        sender (CharField): CharField for the sender type.
        status (CharField): CharField for the status of the message.
        aenderung_typ (CharField): CharField for the type of change.

    Meta:
        verbose_name_plural (str): The plural name for the model.
    """

    class AenderungTypENUM(models.TextChoices):
        """
        Enumeration class representing different types of changes.
        """

        EROEFFNUNG = "01", "Eröffnung"
        ZUWEISUNG = "02", "Zuweisung"
        STATUS = "03", "Statusänderung"
        NACHRICHT = "04", "Nachricht"

    class SenderENUM(models.TextChoices):
        """
        Enumeration class for sender types.

        The SenderENUM class defines the available sender types for messages.
        Each sender type is represented by a code and a corresponding label.
        """

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
        """
        Returns a string representation of the object.

        The string includes the sender (student), recipient (tutor),
        and correction (korrektur) information.
        """
        return f"""Nachricht von {self.student}
            an {self.tutor} für {self.korrektur}"""
