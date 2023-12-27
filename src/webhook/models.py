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
    

# Student model
class Student(models.Model):
    martrikelnummer = models.IntegerField(primary_key=True)
    vorname = models.CharField(max_length=255)
    nachname = models.CharField(max_length=255)
    email = models.EmailField()
    password = models.CharField(max_length=255)

    def __str__(self):
        """String for representating the Model Object."""
        return self.martrikelnummer

# Tutor model
class Tutor(models.Model):
    id = models.IntegerField(primary_key=True)
    vorname = models.CharField(max_length=255)
    nachname = models.CharField(max_length=255)
    email = models.EmailField()
    password = models.CharField(max_length=255)

    def __str__(self):
        """String for representating the Model Object."""
        return self.id  

# Kurs model
class Kurs(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    kurzname = models.CharField(max_length=255)

    def __str__(self):
        """String for representating the Model Object."""
        return self.id

# Korrektur model
class Korrektur(models.Model):
    id = models.IntegerField(primary_key=True)
    typ = models.CharField(max_length=2, choices=KursmaterialEnum.choices)
    ersteller = models.ForeignKey(Student, on_delete=models.CASCADE)
    bearbeiter = models.ForeignKey(Tutor, on_delete=models.CASCADE)
    kurs = models.ForeignKey(Kurs, on_delete=models.CASCADE)

    def __str__(self):
        """String for representating the Model Object."""
        return self.id


# Kursmaterial model
class Kursmaterial(models.Model):
    id = models.IntegerField(primary_key=True)
    typ = models.CharField(max_length=2, choices=KursmaterialEnum.choices)
    kurs = models.ForeignKey(Kurs, on_delete=models.CASCADE)

    def __str__(self):
        """String for representating the Model Object."""
        return self.id

# GedrucktesSkript model
class GedrucktesSkript(models.Model):
    id = models.IntegerField(primary_key=True)
    korrektur = models.ForeignKey(Korrektur, on_delete=models.CASCADE)
    seite = models.CharField(max_length=255)
    beschreibung = models.TextField()

    def __str__(self):
        """String for representating the Model Object."""
        return self.id

# PDFSkript model
class PDFSkript(models.Model):
    id = models.IntegerField(primary_key=True)
    korrektur = models.ForeignKey(Korrektur, on_delete=models.CASCADE)
    seite = models.CharField(max_length=255)
    beschreibung = models.TextField()

    def __str__(self):
        """String for representating the Model Object."""
        return self.id

# IULearnWeb model
class IULearnWeb(models.Model):
    id = models.IntegerField(primary_key=True)
    korrektur = models.ForeignKey(Korrektur, on_delete=models.CASCADE)
    kapitel = models.CharField(max_length=255)
    unterkapitel = models.CharField(max_length=255, null=True)
    beschreibung = models.TextField()

    def __str__(self):
        """String for representating the Model Object."""
        return self.id

# IULearnIPhone model
class IULearnIPhone(models.Model):
    id = models.IntegerField(primary_key=True)
    korrektur = models.ForeignKey(Korrektur, on_delete=models.CASCADE)
    kapitel = models.CharField(max_length=255)
    unterkapitel = models.CharField(max_length=255, null=True)
    beschreibung = models.TextField()

    def __str__(self):
        """String for representating the Model Object."""
        return self.id

# IULearnAndroid model
class IULearnAndroid(models.Model):
    id = models.IntegerField(primary_key=True)
    korrektur = models.ForeignKey(Korrektur, on_delete=models.CASCADE)
    kapitel = models.CharField(max_length=255)
    unterkapitel = models.CharField(max_length=255, null=True)
    beschreibung = models.TextField()

    def __str__(self):
        """String for representating the Model Object."""
        return self.id

# Podcast model
class Podcast(models.Model):
    id = models.IntegerField(primary_key=True)
    korrektur = models.ForeignKey(Korrektur, on_delete=models.CASCADE)
    episode = models.CharField(max_length=255)
    beschreibung = models.TextField()

    def __str__(self):
        """String for representating the Model Object."""
        return self.id

# Video model
class Video(models.Model):
    id = models.IntegerField(primary_key=True)
    korrektur = models.ForeignKey(Korrektur, on_delete=models.CASCADE)
    episode = models.CharField(max_length=255)
    zeit = models.CharField(max_length=255)
    beschreibung = models.TextField()

    def __str__(self):
        """String for representating the Model Object."""
        return self.id

# AllgemeinSonstiges model
class AllgemeinSonstiges(models.Model):
    id = models.IntegerField(primary_key=True)
    korrektur = models.ForeignKey(Korrektur, on_delete=models.CASCADE)
    beschreibung = models.TextField()

    def __str__(self):
        """String for representating the Model Object."""
        return self.id
