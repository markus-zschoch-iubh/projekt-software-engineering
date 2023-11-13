# from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def backend(request):
    return HttpResponse("Hier entsteht das Backend.")
