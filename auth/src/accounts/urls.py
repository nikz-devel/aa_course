from django.urls import path

from .views import SignUpView, UserInfoView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('info', UserInfoView.as_view(), name='userinfo'),
]
