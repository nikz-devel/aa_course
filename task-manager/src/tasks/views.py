from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone
from django.views.generic.list import ListView

from .models import Task


class TasksView(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'tasks_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context
