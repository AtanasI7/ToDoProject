from django.urls import path, include

from tasks.views import TaskCreateView, TaskDetailsView, TaskListView

urlpatterns = [
    path('task/', include([
        path('create/', TaskCreateView.as_view(), name='task-create'),
        path('list', TaskListView.as_view(), name='task-list'),
        path('<int:pk>/', include([
            path('details/', TaskDetailsView.as_view(), name='task-details')
        ]))

    ]))
]