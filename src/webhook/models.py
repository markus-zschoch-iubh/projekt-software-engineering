from django.db import models

# Create your models here.

class Fehlermeldung(models.Model):
    matrikelnummer = models.CharField(max_length=100)
    vorname = models.CharField(max_length=100)
    nachname = models.CharField(max_length=100)
    email = models.EmailField()
    kursabkuerzung = models.CharField(max_length=100)
    medium = models.CharField(max_length=100)
    fehlerbeschreibung = models.TextField()

    def __str__(self):
        return self.matrikelnummer
