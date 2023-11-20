from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hier entsteht das Messaging-Portal zum Austausch zwischen Studierenden und Tutoren.")