import pathlib
import uuid
from django.conf import settings
from django.db import models
from django.utils import timezone
from faker.utils.text import slugify
from users.models import CustomUser


def get_image_path(instance: 'Post', file: str, images_folder=None) -> str:
    if images_folder is None:
        images_folder = settings.MEDIA_ROOT
    post_id = instance.id
    path = pathlib.Path(file)
    file_name_normalize = slugify(path.stem)
    return f"{images_folder}/{post_id}_{file_name_normalize}{path.suffix}"


class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    description = models.CharField(max_length=255, null=True)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    likes = models.ManyToManyField(CustomUser, related_name='likes')
    comments = models.ForeignKey('Comment', on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(default=timezone.now)


class Image(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to=get_image_path, null=True)


class Comment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    text = models.TextField(max_length=255)
    post_reference = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
