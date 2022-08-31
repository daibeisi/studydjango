from django.urls import path
from . import views

app_name = 'Apps.base'

urlpatterns = [
    path("login/", views.user_login),
]
