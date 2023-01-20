from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    context = {}
    return render(request, 'reco/templates/index.html', context)

def pdf(request):
    context = {}
    return render(request, 'reco/templates/pdf.html', context)

def word(request):
    context = {}
    return HttpResponse(request)
