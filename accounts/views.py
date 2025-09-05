from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.forms import modelform_factory
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from accounts.forms import ToDoUserBaseForm, ToDoUserDeleteForm, ToDoUserEditForm
from tasks.models import Task

UserModel = get_user_model()


def home_page_view(request):
    return render(request, 'common/home.html')

class RegisterUserView(CreateView):
    form_class = ToDoUserBaseForm
    success_url = reverse_lazy('home-page')
    template_name = 'registration/register.html'

class UserDetailsView(LoginRequiredMixin, DetailView):
    model = UserModel
    template_name = 'accounts/profile-details.html'

class UserEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = UserModel
    template_name = 'accounts/profile-edit.html'
    form_class = ToDoUserEditForm
    # success_url = reverse_lazy('profile-details')

    def get_success_url(self):
        return reverse_lazy('profile-details', kwargs={"pk": self.object.pk})

    def test_func(self):
        return self.request.user.pk == self.kwargs['pk']

    def get_form_class(self):
        if self.request.user.is_superuser:
            return modelform_factory(UserModel, fields='__all__')

        return modelform_factory(UserModel, fields='__all__')

class UserDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = UserModel
    template_name = 'accounts/profile-delete.html'
    success_url = reverse_lazy('home-page')
    form_class = ToDoUserDeleteForm

    def test_func(self):
        return self.request.user.pk == self.kwargs['pk']

    def get_initial(self):
        pk = self.kwargs.get(self.pk_url_kwarg)
        task = self.model.objects.get(pk=pk)

        return task.__dict__