from django.urls import path
from . import views

# 二级URL设置
urlpatterns = [
    path('', views.index),
    path("test/", views.test),
    path("time/", views.time),
]
