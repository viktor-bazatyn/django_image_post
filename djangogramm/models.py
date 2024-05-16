import pathlib
import uuid
from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from faker.utils.text import slugify


class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    biography = models.TextField(null=True)
    avatar = models.ImageField(upload_to='avatars', null=True)
    email = models.EmailField(unique=True)


def get_image_path(instance: 'Post',
                   file: pathlib.Path,
                   images_folder=None) -> pathlib.Path:
    if images_folder is None:
        images_folder = settings.MEDIA_ROOT
    post_id = instance.id
    file_name_normalize = slugify(file.stem)
    return images_folder / f"{post_id}{file_name_normalize}{file.suffix}"


class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    description = models.CharField(max_length=255, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name='likes')
    comments = models.ForeignKey('Comment', on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(default=timezone.now)


class Image(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to=get_image_path, null=True)


class Like(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)


class Comment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    text = models.TextField(max_length=255)
    post_reference = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
