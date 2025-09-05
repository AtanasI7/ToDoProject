from django import forms
from django.core.exceptions import ValidationError
from django.forms.formsets import formset_factory
from django.utils.timezone import now

from tasks.mixins import ReadOnlyMixin
from tasks.models import Task, Comment


class TaskBaseForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date', 'status', 'priority']
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'placeholder': 'Enter title...'
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'placeholder': 'Enter description...'
                }
            ),
            'due_date': forms.DateInput(
                attrs={
                    'type': 'date'
                }
            ),
            'status': forms.RadioSelect(
                attrs={
                    'disabled': True
                }
            ),
            'priority': forms.RadioSelect()
        }

    def clean_due_date(self):
        due_date = self.cleaned_data.get('due_date')

        if due_date is None:
            raise ValidationError("Insert a due date!")

        if due_date < now():
            raise ValidationError("The due date must not be before today's date!")


        return due_date

class TaskCreateForm(TaskBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['status'].disabled = True

class TaskEditForm(TaskBaseForm):
    pass

class TaskDeleteForm(ReadOnlyMixin, TaskBaseForm):
    pass

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields =['content']
        labels = {
            'content': ''
        }

        widgets = {
            'content': forms.TextInput(
                attrs={
                    'placeholder': 'Add a comment...'
                }
            )
        }

CommentFormSet = formset_factory(CommentForm, extra=1)


