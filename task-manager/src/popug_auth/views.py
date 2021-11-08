from django.http.response import HttpResponse, HttpResponseRedirect
from django.views import View
from django.conf import settings
from django.contrib.auth import login
import requests

from .models import User

class AuthorizeCallbackView(View):
    def get(self, request):
        code = request.GET.get('code')
        if not code:
            return HttpResponseRedirect(settings.LOGIN_URL)
        
        data = {
            "client_id": settings.CLIENT_ID,
            "client_secret": settings.CLIENT_SECRET,
            "code": code,
            "redirect_uri": settings.AUTH_CALLBACK,
            "grant_type": "authorization_code",
        }
        list_data = []
        for key, value in data.items():
            list_data.append(f"{key}={value}")
        
        resp = requests.post(
            settings.AUTH_TOKEN_URL,
            data="&".join(list_data),
            headers={"Content-Type": "application/x-www-form-urlencoded"},
        )

        data = resp.json()
        token = data.get("access_token")
        if not token:
            return HttpResponseRedirect(settings.LOGIN_URL)

        external_user = requests.get(settings.AUTH_USERINFO_URL, headers={"Authorization": f"Bearer {token}"}).json()

        user = User.objects.filter(uuid=external_user["uuid"]).first()
        if not user:
            return HttpResponse("Ошибка авторизации")
        
        login(request, user)
        return HttpResponseRedirect("/")
