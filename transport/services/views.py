from django.shortcuts import render
from . models import Technique


def index(request):
    template = 'services/index.html'
    title = 'Транспорт - Главная'
    context = {
        'title': title,
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
    template = 'services/contacts.html'
    title = 'Транспорт - Контакты'
    context = {
        'title': title,
        'text': 'Здесь будут все контакты, адреса и прочие координаты организации'
    }
    return render(request, template, context)