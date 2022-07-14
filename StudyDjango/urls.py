"""StudyDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView
from django.conf import settings
from django.conf.urls.static import static


# Django 自带后台管理系统名称修改
admin.site.site_header = '呆贝斯管理系统'
admin.site.site_title = '呆贝斯管理系统'
# admin.site.index_title = '我在浏览器标签前面'


urlpatterns = [
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('favicon.ico', RedirectView.as_view(url='/static/favicon.ico')),
    path('', include('Apps.base.urls', namespace="base")),
    path('company/', include('Apps.company.urls', namespace="company")),
    path('blog/', include('Apps.blog.urls', namespace="blog")),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
              + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
