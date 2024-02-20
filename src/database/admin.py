from django.contrib import admin

from .models import (
    Korrektur,
    Kurs,
    Kursmaterial,
    Student,
    Tutor,
    Messages,
)

# Register your models here.


class KorrekturAdmin(admin.ModelAdmin):
    """
    Admin class for managing Korrektur model in the database.
    """

    list_display = (
        "ersteller",
        "kursmaterial",
        "bearbeiter",
    )
    list_filter = (
        "ersteller",
        "kurs",
        "kursmaterial",
        "bearbeiter",
    )


class KursmaterialAdmin(admin.ModelAdmin):
    """
    Admin class for managing Kursmaterial objects.
    """

    list_display = (
        "typ",
        "kurs",
    )
    list_filter = (
        "typ",
        "kurs",
    )


admin.site.register(Korrektur, KorrekturAdmin)
admin.site.register(Kurs)
admin.site.register(Kursmaterial, KursmaterialAdmin)
admin.site.register(Student)
admin.site.register(Tutor)
admin.site.register(Messages)
