from django.contrib import admin
from django.urls import path, include

from .views import TasksView

urlpatterns = [
    path('', TasksView.as_view(), name='tasks'),
]