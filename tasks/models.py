from django.contrib.auth import get_user_model
from django.db import models
from tasks.choices import TaskStatusChoices, TaskPriorityChoices
from tasks.validators import BadWordValidator

UserModel = get_user_model()


class Task(models.Model):
    title = models.CharField(
        max_length=100,
        validators=[
            BadWordValidator(
                bad_words=[
                    'fuck',
                    'shit',
                    'damn'
                ]
            )
        ],
    )
    description = models.TextField(
        blank=True,
        null=True,
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
    )
    due_date = models.DateTimeField(
        null=True,
        blank=True,
    )
    status = models.CharField(
        max_length=30,
        choices=TaskStatusChoices.choices,
        default=TaskStatusChoices.PENDING,
    )
    priority = models.CharField(
        max_length=30,
        choices=TaskPriorityChoices.choices,
        default=TaskPriorityChoices.LOW,
    )
    author = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
        related_name='tasks'
    )
    is_approved = models.BooleanField(
        default=False
    )

    def __str__(self):
        return self.title

class Comment(models.Model):
    content = models.TextField()
    author = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    task = models.ForeignKey(
        Task,
        on_delete=models.CASCADE,
        related_name='comments'
    )

    def __str__(self):
        return self.content