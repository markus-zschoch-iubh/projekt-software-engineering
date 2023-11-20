from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hier entsteht der Webhook, der Korrekturen entgegennimmt.")