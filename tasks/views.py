from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView

from tasks.forms import CommentFormSet, TaskCreateForm, TaskEditForm
from tasks.models import Task


class TaskCreateView(CreateView):
    model = Task
    form_class = TaskCreateForm
    template_name = 'tasks/create_task.html'
    success_url = reverse_lazy('home-page')

    def form_valid(self, form):
        form.instance.author_id = self.request.user.pk
        return super().form_valid(form)

class TaskDetailsView(DetailView):
    model = Task
    template_name = 'tasks/details-task.html'

    def get_queryset(self):
        return Task.objects.filter(author=self.request.user)
class TaskListView(ListView):
    model = Task
    template_name = 'tasks/list-task.html'

    def get_queryset(self):
        return Task.objects.filter(author=self.request.user)
