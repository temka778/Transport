from django.http import Http404


class AjaxOnlyMixin:
    """
    Миксин для обработки только AJAX-запросов.
    Возвращает 404 для не-AJAX-запросов.
    """
    def dispatch(self, request, *args, **kwargs):
        if not request.headers.get('x-requested-with') == 'XMLHttpRequest':
            raise Http404("Страница не найдена")
        return super().dispatch(request, *args, **kwargs)