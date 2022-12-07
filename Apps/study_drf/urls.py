from django.urls import include, path
from rest_framework import routers
from . import views
app_name = 'Apps.study_drf'

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('snippets/', views.snippet_list),
    path('snippets/<int:pk>/', views.snippet_detail),
]