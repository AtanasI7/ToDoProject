from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView
from accounts.forms import ToDoUserCreationForm

UserModel = get_user_model()


def home_page_view(request):
    return render(request, 'common/home.html')

class RegisterUserView(CreateView):
    form_class = ToDoUserCreationForm
    success_url = reverse_lazy('home-page')
    template_name = 'registration/register.html'

class UserDetailsView(DetailView):
    model = UserModel
    template_name = 'accounts/profile-details.html'
