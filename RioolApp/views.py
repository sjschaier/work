from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse



def landing(request):
    return render(request, "landing.html")

def nieuw_model(request):
    return render(request, 'nieuw_model.html')

def overzicht(request):
    return render(request, 'overzicht.html')

def meerjarenplanning(request):
    return render(request, 'meerjarenplanning.html')

def standaard_beoordeling(request):
    return render(request, 'standaard_beoordeling.html')