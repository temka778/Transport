from django.shortcuts import render
from . models import Technique
from django.views.generic.detail import DetailView


def index(request):
    template = 'services/index.html'
    technique = Technique.objects.all()
    context = {'technique': technique}
    return render(request, template, context)


class TechniqueDetail(DetailView):
    model = Technique
    template_name = 'services/technique_detail.html'
    context_object_name = 'technique'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['photos'] = self.object.photos.all()
        context['is_authenticated'] = self.request.user.is_authenticated
        return context