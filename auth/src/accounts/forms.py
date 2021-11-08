from .events import UserCreatedEvent
from django.contrib.auth.forms import UserCreationForm, UsernameField

from .models import User


class CreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username",)
        field_classes = {'username': UsernameField}

    def save(self, commit=True):
        user = super().save()
        UserCreatedEvent(user).send()
        return user
