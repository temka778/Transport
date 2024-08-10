from django.urls import reverse_lazy
from django.views.generic import CreateView #, DetailView
#from django.shortcuts import render, get_object_or_404

from .forms import CreationForm
#from .models import User


app_name = 'users'


class SignUp(CreateView):
    form_class = CreationForm
    success_url = reverse_lazy('services:index')
    template_name = 'users/signup.html'


#class Personal_account(DetailView):
    #data = User.objects.all()
    #data = get_object_or_404(User, pk=pk)
    #model = User
    #template = 'users/personal_account.html'
    #context_object_name = 'user'
    #context = {
    #    'title': 'Личный кабинет',
    #    'data': get_object_or_404(User, pk='pk')
    #}
    #return render(request, template, context)

#def personal_account(request, pk):
#    user = get_object_or_404(User, id=pk)
#    context = {'user': user}
#    return render(request, 'users/personal_account.html', context)