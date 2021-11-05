
from django.urls import path

from .views import AuthorizeCallbackView

urlpatterns = [
    path('callback', AuthorizeCallbackView.as_view(), name='callback'),
]