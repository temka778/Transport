from django.shortcuts import render
from . models import Technique


def index(request):
    template = 'services/index.html'
    technique = Technique.objects.all()
    context = {'technique': technique}
    return render(request, template, context)