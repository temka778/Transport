import datetime
from django.shortcuts import render


def index(request):
    template = 'services/index.html'
    title = 'Транспорт - Главная'
    context = {
        'title': title,
        'text': 'Здесь будет информация о компании, картинки, текст различных.....',
        'year': datetime.datetime.now().year
    }
    return render(request, template, context)


def services(request):
    template = 'services/services.html'
    title = 'Транспорт - Услуги'
    context = {
        'title': title,
        'text': 'Здесь будет перечень всех предоставляемых услуг...',
    }
    return render(request, template, context)


def contacts(request):
    template = 'services/contacts.html'
    title = 'Транспорт - Контакты'
    context = {
        'title': title,
        'text': 'Здесь будут все контакты, адреса и прочие координаты организации',
    }
    return render(request, template, context)