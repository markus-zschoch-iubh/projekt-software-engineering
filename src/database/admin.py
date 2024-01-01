from django.contrib import admin

from .models import (
    Korrektur,
    GedrucktesSkript,
    PDFSkript,
    IULearnWeb,
    IULearnAndroid,
    IULearnIPhone,
    Podcast,
    Video,
    AllgemeinSonstiges,
    Kurs,
    Kursmaterial,
    Student,
    StudentKurs,
    Tutor,
)

# Register your models here.
admin.site.register(Korrektur)
admin.site.register(GedrucktesSkript)
admin.site.register(PDFSkript)
admin.site.register(IULearnWeb)
admin.site.register(IULearnAndroid)
admin.site.register(IULearnIPhone)
admin.site.register(Podcast)
admin.site.register(Video)
admin.site.register(AllgemeinSonstiges)
admin.site.register(Kurs)
admin.site.register(Kursmaterial)
admin.site.register(Student)
admin.site.register(StudentKurs)
admin.site.register(Tutor)
