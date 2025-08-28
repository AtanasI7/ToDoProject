from django.db import models


class TaskStatusChoices(models.TextChoices):
    PENDING = 'Pending', 'Pending'
    IN_PROGRESS = 'In Progress', 'In Progress'
    COMPLETED = 'Completed', 'Completed'

class TaskPriorityChoices(models.TextChoices):
    LOW = 'Low', 'Low'
    MEDIUM = 'Medium', 'Medium'
    HIGH = 'High', 'High'