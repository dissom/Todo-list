from django.urls import path

from todo.views import (
    index,
    TagDeleteView,
    TagUpdateView,
    TaskDeleteView,
    TaskStatusUpdateView,
    TaskUpdateView,
    TagListView,
    TaskCreateView,
    TagCreateView,
)


urlpatterns = [
    path(
        "",
        index,
        name="index"
    ),
    path(
        "tasks/create/",
        TaskCreateView.as_view(),
        name="task-create"
    ),
    path(
        "tasks/<int:pk>/update/",
        TaskUpdateView.as_view(),
        name="task-update"
    ),
    path(
        "task/<int:pk>/update-status/",
        TaskStatusUpdateView.as_view(),
        name="task-status-update",
    ),
    path(
        "task/<int:pk>/delete/",
        TaskDeleteView.as_view(),
        name="task-delete"
    ),
    path(
        "tags/",
        TagListView.as_view(),
        name="tags-list"
    ),
    path(
        "tag/create/",
        TagCreateView.as_view(),
        name="tag-create"
    ),
    path(
        "tag/<int:pk>/update/",
        TagUpdateView.as_view(),
        name="tag-update"
    ),
    path(
        "tag/<int:pk>/delete/",
        TagDeleteView.as_view(),
        name="tag-delete"
    ),
]


app_name = "todo"
