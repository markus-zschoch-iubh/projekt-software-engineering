# from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def webhook(request):
    return HttpResponse("Hier entsteht der Webhook - Nothing to see.")
