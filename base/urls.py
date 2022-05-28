from django.urls import path
from django.views.generic import RedirectView
from django.templatetags.static import static
from . import views


# 二级URL设置
urlpatterns = [
    path('', views.index),
    path("test/", views.test),
    path("time/", views.time),
    path('favicon.ico', RedirectView.as_view(url=static('favicon.ico'))),
]
