from django.shortcuts import render
from . models import Technique


def index(request):
    template = 'services/index.html'
    return render(request, template)


def services(request):
    template = 'services/services.html'
    technique = Technique.objects.all()
    context = {'technique': technique}
    return render(request, template, context)


def contacts(request):
    template = 'services/contacts.html'
    return render(request, template)