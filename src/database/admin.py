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
admin.register(Korrektur)
admin.register(GedrucktesSkript)
admin.register(PDFSkript)
admin.register(IULearnWeb)
admin.register(IULearnAndroid)
admin.register(IULearnIPhone)
admin.register(Podcast)
admin.register(Video)
admin.register(AllgemeinSonstiges)
admin.register(Kurs)
admin.register(Kursmaterial)
admin.register(Student)
admin.register(StudentKurs)
admin.register(Tutor)
