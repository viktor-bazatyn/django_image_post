import uuid

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


class User(AbstractUser):
    biography = models.TextField(blank=True)
    avatar = models.ImageField(upload_to='avatars')
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email


class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    description = models.CharField(blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='posts')
    likes = models.ManyToManyField(User, related_name='likes', blank=True)
    comments = models.ManyToManyField(Comment, related_name='comments', blank=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Post by {self.author.email}"


class Comment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    text = models.TextField(blank=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Comment by {self.author.email}"


class Picture(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    image = models.ImageField(upload_to='pictures')
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return f"Picture for post {self.post.id}"
