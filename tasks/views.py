from django.forms.models import modelform_factory
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, UpdateView, DeleteView
from django.views.generic.edit import FormMixin

from tasks.forms import CommentFormSet, TaskCreateForm, TaskEditForm, TaskDeleteForm
from tasks.models import Task, Comment


class TaskCreateView(CreateView):
    model = Task
    form_class = TaskCreateForm
    template_name = 'tasks/create_task.html'
    success_url = reverse_lazy('home-page')

    def form_valid(self, form):
        form.instance.author_id = self.request.user.pk
        return super().form_valid(form)

class TaskEditView(UpdateView):
    model = Task
    template_name = 'tasks/edit-task.html'
    success_url = reverse_lazy('task-details', )

    def get_form_class(self):
        if self.request.user.is_superuser:
            return modelform_factory(Task, fields='__all__')

        return modelform_factory(Task, fields=['description', 'status', 'priority'])

class TaskDetailsView(DetailView, FormMixin):
    model = Task
    template_name = 'tasks/details-task.html'
    form_class = CommentFormSet

    def get_queryset(self):
        return Task.objects.filter(author=self.request.user)

    def get_context_data(self, **kwargs):
        kwargs.update({
            'comment_form_set': self.get_form_class()()
        })
        
        return super().get_context_data(**kwargs)

    def get_success_url(self):
        return reverse_lazy('task-details', kwargs={'pk': self.kwargs.get(self.pk_url_kwarg)})

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        comment_form_set = self.get_form_class()(request.POST)

        if comment_form_set.is_valid():
            for comment_form in comment_form_set:
                comment: Comment = comment_form.save(commit=False)
                comment.task = self.object
                comment.author = request.user
                comment.save()

            return self.form_valid(comment_form_set)

        return None

class TaskListView(ListView):
    model = Task
    template_name = 'tasks/list-task.html'

    def get_queryset(self):
        return Task.objects.filter(author=self.request.user)

class TaskDeleteView(DeleteView):
    model = Task
    form_class = TaskDeleteForm
    success_url = reverse_lazy('task-list')
    template_name = 'tasks/delete-task.html'

    def get_initial(self):
        pk = self.kwargs.get(self.pk_url_kwarg)
        task = self.model.objects.get(pk=pk)

        return task.__dict__
