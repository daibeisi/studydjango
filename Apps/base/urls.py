from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

app_name = 'Apps.base'


urlpatterns = [
    path('routers/', views.router_list, name='router-list'),
    path('countries/', views.country_list, name='country-list'),
    path('countries/<int:pk>/', views.country_detail, name='country-detail'),
    path('provinces/', views.ProvinceList.as_view(), name='province-list'),
    path('provinces/<int:pk>/', views.ProvinceDetail.as_view(), name='province-detail'),
    path('cities/', views.CityList.as_view(), name='city-list'),
    path('cities/<int:pk>/', views.CityDetail.as_view(), name='city-detail'),
    path('areas/', views.AreaList.as_view(), name='area-list'),
    path('areas/<int:pk>/', views.AreaDetail.as_view(), name='area-detail'),
    path('towns/', views.TownList.as_view(), name='town-list'),
    path('towns/<int:pk>/', views.TownDetail.as_view(), name='town-detail'),
    path("register", views.RegisterView.as_view(), name='register'),
    path("login", views.LoginView.as_view(), name='login'),
]

urlpatterns = format_suffix_patterns(urlpatterns)

# 增加的条目
handler400 = views.bad_request
handler403 = views.permission_denied
handler404 = views.page_not_found
handler500 = views.error
