from django.urls import path

from .views import (
    UserRegisterView, UserLoginView, logOutView
)

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='user-register'),

    path('login/', UserLoginView.as_view(), name='user-login'),

    path('logout/', logOutView, name='user-logout'),

    
    
]