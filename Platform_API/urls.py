from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .views import PostViewSet, TaskViewSet

router = routers.DefaultRouter()
router.register('Posts', PostViewSet)
router.register('Tasks', TaskViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]