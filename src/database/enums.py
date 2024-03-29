from django.db import models


class KursstatusEnum(models.TextChoices):
    """
    Enum representing the status of a course.
    """

    AKTIV = "01", "Aktiv"
    ABGESCHLOSSEN = "02", "Abgeschlossen"


class KursmaterialEnum(models.TextChoices):
    """
    Enum class representing the different types of course materials.
    """

    GEDRUCKTES_SKRIPT = "01", "Gedrucktes Skript"
    PDF_SKRIPT = "02", "PDF Skript"
    IU_LEARN_WEB = "03", "IU Learn (Web)"
    IU_LEARN_IPHONE = "04", "IU Learn (iPhone)"
    IU_LEARN_ANDROID = "05", "IU Learn (Android)"
    PODCAST = "06", "Podcast"
    VIDEO = "07", "Video"
    SONSTIGES_ALLGEMEIN = "08", "Sonstiges/Allgemein"

    def __str__(self):
        return self.label


class KorrekturstatusEnum(models.TextChoices):
    """
    Enumeration class for the status of corrections.
    """

    OFFEN = "01", "Offen"
    BEARBEITUNG = "02", "In Bearbeitung"
    UMGESETZT = "03", "Umgesetzt"
    ABGELEHNT = "04", "Abgelehnt"

    def __str__(self):
        return self.label
