from django.urls import path
from . import views

app_name = 'Apps.base'

urlpatterns = [
    path("register", views.RegisterView.as_view(), name='register'),
    path("login", views.LoginView.as_view(), name='login'),
]