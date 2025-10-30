from rest_framework import serializers
from .models import Post, Task


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        
        model = Post

        fields = '__all__'

        #OR
        #field - '__all__'

class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = '__all__'