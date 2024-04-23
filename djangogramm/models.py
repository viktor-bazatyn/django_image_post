import uuid

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from faker.utils.text import slugify


class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    biography = models.TextField(blank=True)
    avatar = models.ImageField(upload_to='avatars')
    email = models.EmailField(unique=True)


def get_image_path(instance, filename):
    post_id = instance.id
    filename = slugify(filename, allow_unicode=True)
    return f'posts/{post_id}/{filename}'


class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    description = models.CharField(max_length=255, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=get_image_path)
    likes = models.ManyToManyField(User, related_name='likes', blank=True)
    comments = models.ForeignKey('Comment', on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)


class Like(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)


class Comment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    text = models.TextField(blank=True)
    post_reference = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
