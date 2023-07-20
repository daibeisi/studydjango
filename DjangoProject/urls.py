"""
URL configuration for DjangoProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from DjangoProject.rest_framework import router
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    # TokenObtainSlidingView,
    # TokenRefreshSlidingView,
    TokenBlacklistView,
    TokenVerifyView
)


# Django 自带后台管理系统名称修改
admin.site.site_header = "Django管理系统"
admin.site.site_title = "Django管理系统"
# admin.site.index_title = '我在浏览器标签前面'

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/base/', include('Apps.base.urls', namespace='base')),
    # path('api/sliding-token/', TokenObtainSlidingView.as_view(), name='token_obtain_pair'),
    # path('api/sliding-token/refresh/', TokenRefreshSlidingView.as_view(), name='token_refresh'),
    path('api/token/blacklist/', TokenBlacklistView.as_view(), name='token_blacklist'),
    path('api/token/verify/', TokenVerifyView.as_view(), name="token_verify"),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api-auth/api-router/', include(router.urls)),
    path('favicon.ico', RedirectView.as_view(url='/static/favicon.ico')),
    path("admin/", admin.site.urls),
    path("", RedirectView.as_view(url='/admin/login')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
