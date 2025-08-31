from django.urls import path, include

from tasks.views import TaskCreateView, TaskDetailsView, TaskListView, TaskEditView, TaskDeleteView

urlpatterns = [
    path('task/', include([
        path('create/', TaskCreateView.as_view(), name='task-create'),
        path('list/', TaskListView.as_view(), name='task-list'),
        path('<int:pk>/', include([
            path('details/', TaskDetailsView.as_view(), name='task-details'),
            path('edit/', TaskEditView.as_view(), name='task-edit'),
            path('delete/', TaskDeleteView.as_view(), name='task-delete'),
        ]))

    ]))
]