from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import PostViewSet, CommentViewSet
from drf_yasg import openapi
from drf_yasg.views import get_schema_view


router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)

schema_view = get_schema_view(
   openapi.Info(
      title="Blogging Platform API",
      default_version='v1',
      description="API endpoints for managing blog posts and comments.",
      contact=openapi.Contact(email="support@myblog.com"),
      license=openapi.License(name="MIT License"),
   ),
   public=True,
)

urlpatterns = [
    path('', include(router.urls)),
]
