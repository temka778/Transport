from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'services/index.html')


def services(request):
    return render(request, 'services/services.html')


def contacts(request):
    return render(request, 'services/contacts.html')