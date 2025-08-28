from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from accounts.forms import ToDoUserCreationForm


def home_page_view(request):
    return render(request, 'common/home.html')

class RegisterUserView(CreateView):
    form_class = ToDoUserCreationForm
    success_url = reverse_lazy('home-page')
    template_name = 'registration/register.html'
