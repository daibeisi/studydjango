from django.urls import path
from django.views.generic import RedirectView
from django.templatetags.static import static
from django.views.static import serve
from StudyDjango.settings import MEDIA_ROOT
from . import views

# 二级URL设置
urlpatterns = [
    # TODO:将网站图标和上传地址搬移到项目urls中
    path('favicon.ico', RedirectView.as_view(url=static('favicon.ico'))),
    path('', views.index),
    path("test/", views.test),
    path("time/", views.time),
    path("filter/", views.test_filter),
    path("tag/", views.test_simpletag),
    path("base/", views.base),
    path("inhert_base/", views.inhert_base),
    path("include/", views.test_include),
    path('upload/<str:path>/', serve, {"document_root":MEDIA_ROOT}),
]
