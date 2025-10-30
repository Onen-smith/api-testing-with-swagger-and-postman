from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

def __str__(self):
    return self.name

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.CharField(max_length=100)
    created_at = models.DateField(auto_now=True)
    updated_at = models.DateField(auto_now=True)
    
def __str__(self):
    return self.title


class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    commenter = models.TextField(max_length=20)

def __str__(self):
    return self.commenter