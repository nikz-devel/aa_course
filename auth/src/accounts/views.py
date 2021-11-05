from django.http import JsonResponse
from django.http.response import HttpResponseForbidden
from django.urls import reverse_lazy
from django.views import generic
from oauth2_provider.views.generic import ProtectedResourceView

from .forms import CreationForm


class SignUpView(generic.CreateView):
    form_class = CreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


class ProtectedApiView(ProtectedResourceView):
    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        if isinstance(response, HttpResponseForbidden):
            return JsonResponse({"error": "auth error"})
        
        return response
    

class UserInfoView(ProtectedApiView):
    def get(self, request, *args, **kwargs):
        userinfo = {
            "username": request.resource_owner.username,
            "email": request.resource_owner.email,
            "uuid": request.resource_owner.uuid,
        }
        return JsonResponse(userinfo)
