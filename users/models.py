from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid


def get_avatar_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = f"{uuid.uuid4()}.{ext}"
    return f'avatars/{filename}'


class CustomUser(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    biography = models.TextField(null=True)
    avatar = models.ImageField(upload_to=get_avatar_path, null=True)
    email = models.EmailField(unique=True)
