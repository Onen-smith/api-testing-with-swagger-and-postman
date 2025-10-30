from rest_framework import viewsets
from .models import Post, Task
from .serializers import PostSerializer, TaskSerializer

class PostViewSet(viewsets.ModelViewSet):

    queryset = Post.objects.all()

    serializer_class = PostSerializer

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all().order_by('-created_at')
    serializer_class = TaskSerializer