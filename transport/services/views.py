from django.shortcuts import render
from . models import Technique


def index(request):
    template = 'services/index.html'
    context = {
        'title': 'Транспорт - Главная',
        'heading': 'О компании',
        'text': 'Здесь будет информация о компании, картинки, текст различных.....'
    }
    return render(request, template, context)


def services(request):
    template = 'services/services.html'
    title = 'Транспорт - Услуги'
    technique = Technique.objects.all()
    context = {
        'title': title,
        'technique': technique
    }
    return render(request, template, context)


def contacts(request):
    template = 'services/index.html'
    context = {
        'title': 'Транспорт - Контакты',
        'heading': 'Контакты',
        'text': 'Здесь будут все контакты, адреса и прочие координаты организации'
    }
    return render(request, template, context)