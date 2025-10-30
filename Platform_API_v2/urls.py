from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .views import PostViewSet, TaskViewSet, CommentViewSet
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="My API",
        default_version='v1',
        description="API documentation for my project",
        contact=openapi.Contact(email="your@email.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
path('swagger.json', schema_view.without_ui(cache_timeout=0), name='schema-json'),

router = routers.DefaultRouter()
router.register('Posts', PostViewSet)
router.register('Tasks', TaskViewSet)
router.register('Comment', CommentViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]