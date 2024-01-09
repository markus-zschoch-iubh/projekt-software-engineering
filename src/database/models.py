from django.db import models
from django.utils import timezone
from .enums import KursmaterialEnum, KursstatusEnum, KorrekturstatusEnum

# Create your models here.

class Kurs(models.Model):
    name = models.CharField(max_length=255)
    kurzname = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.kurzname} - {self.name}"


class Kursmaterial(models.Model):
    typ = models.CharField(max_length=2, choices=KursmaterialEnum.choices)
    kurs = models.ForeignKey(Kurs, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.typ} - {self.kurs}"


class Student(models.Model):
    martrikelnummer = models.IntegerField(primary_key=True)
    vorname = models.CharField(max_length=255)
    nachname = models.CharField(max_length=255)
    email = models.EmailField()
    password = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.nachname}, {self.vorname} ({self.martrikelnummer})"


class StudentKurs(models.Model):
    martrikelnummer: models.ForeignKey(
        Student, on_delete=models.CASCADE, null=True
    )
    kursId = models.ForeignKey(Kurs, on_delete=models.CASCADE, null=True)
    status: models.CharField(max_length=2, choices=KursstatusEnum.choices)


class Tutor(models.Model):
    vorname = models.CharField(max_length=255)
    nachname = models.CharField(max_length=255)
    email = models.EmailField()
    password = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.nachname}, {self.vorname}"


class Korrektur(models.Model):
    typ = models.CharField(max_length=2, choices=KursmaterialEnum.choices)
    ersteller = models.ForeignKey(Student, on_delete=models.CASCADE)
    bearbeiter = models.ForeignKey(
        Tutor, on_delete=models.CASCADE, blank=True, null=True
    )
    kurs = models.ForeignKey(Kurs, on_delete=models.CASCADE)
    #kursmaterial = models.ForeignKey(Kursmaterial, on_delete=models.CASCADE)
    aktuellerStatus = models.CharField(
        max_length=2,
        choices=KorrekturstatusEnum.choices,
        default=KorrekturstatusEnum.OFFEN
    )
    fehler_beschreibung = models.TextField(default="Keine Beschreibung")

class Messages(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='student_messages')
    tutor = models.ForeignKey(Tutor, on_delete=models.CASCADE, related_name='tutor_messages')
    korrektur = models.ForeignKey(Korrektur, on_delete=models.CASCADE, related_name='korrektur_messages')
    text = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"Nachricht von {self.student} an {self.tutor} für {self.korrektur}"

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


# GedrucktesSkript model
class GedrucktesSkript(models.Model):
    korrektur = models.OneToOneField(Korrektur, on_delete=models.CASCADE)
    seite = models.CharField(max_length=255)
    beschreibung = models.TextField()

    def __str__(self):
        return str(self.id)


# PDFSkript model
class PDFSkript(models.Model):
    korrektur = models.OneToOneField(Korrektur, on_delete=models.CASCADE)
    seite = models.CharField(max_length=255)
    beschreibung = models.TextField()

    def __str__(self):
        return str(self.id)


# IULearnWeb model
class IULearnWeb(models.Model):
    id = models.IntegerField(primary_key=True)
    korrektur = models.OneToOneField(Korrektur, on_delete=models.CASCADE)
    kapitel = models.CharField(max_length=255)
    unterkapitel = models.CharField(max_length=255, null=True)
    beschreibung = models.TextField()

    def __str__(self):
        return str(self.id)


# IULearnIPhone model
class IULearnIPhone(models.Model):
    korrektur = models.OneToOneField(Korrektur, on_delete=models.CASCADE)
    kapitel = models.CharField(max_length=255)
    unterkapitel = models.CharField(max_length=255, null=True)
    beschreibung = models.TextField()

    def __str__(self):
        return str(self.id)


# IULearnAndroid model
class IULearnAndroid(models.Model):
    korrektur = models.OneToOneField(Korrektur, on_delete=models.CASCADE)
    kapitel = models.CharField(max_length=255)
    unterkapitel = models.CharField(max_length=255, null=True)
    beschreibung = models.TextField()

    def __str__(self):
        return str(self.id)


# Podcast model
class Podcast(models.Model):
    korrektur = models.OneToOneField(Korrektur, on_delete=models.CASCADE)
    episode = models.CharField(max_length=255)
    beschreibung = models.TextField()

    def __str__(self):
        return str(self.id)


# Video model
class Video(models.Model):
    korrektur = models.OneToOneField(Korrektur, on_delete=models.CASCADE)
    episode = models.CharField(max_length=255)
    zeit = models.CharField(max_length=255)
    beschreibung = models.TextField()

    def __str__(self):
        return str(self.id)


# AllgemeinSonstiges model
class AllgemeinSonstiges(models.Model):
    korrektur = models.OneToOneField(Korrektur, on_delete=models.CASCADE)
    beschreibung = models.TextField()

    def __str__(self):
        return str(self.id)