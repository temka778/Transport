from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse('Главненькая страница')

def twoo_pages(request, pk):
    return HttpResponse(f'Страничка № {pk}!')

def group_posts(request, post_1):
    return HttpResponse(f'Страничка ({post_1}), на которой будут посты, \
        отфильтрованные по группам. \
        Уряя!! У меня что-то получается даже)))) \
        ПЕРВЫЙ ПОСТ!!!!')