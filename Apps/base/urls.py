from django.urls import path
from . import views
app_name = 'Apps.base'

# 二级URL设置
urlpatterns = [
    path('', views.index),
    path("test/", views.test),
    path("time/", views.time),
    path("filter/", views.test_filter),
    path("tag/", views.test_simpletag),
    path("base/", views.base),
    path("inhert_base/", views.inhert_base),
    path("include/", views.test_include),
    path("test1/", views.test_process_template_response),
]
