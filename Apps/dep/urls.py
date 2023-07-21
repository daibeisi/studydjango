from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

app_name = 'Apps.dep'


urlpatterns = [
    path('departments/', views.DepartmentList.as_view(), name='department-list'),
    path('departments/<int:pk>/', views.DepartmentDetail.as_view(), name='department-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
