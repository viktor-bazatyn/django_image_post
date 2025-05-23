import os
import pathlib

import django
from faker import Faker
import random
from django.core.files import File
from django.contrib.auth import get_user_model
from base import settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "base.settings")

django.setup()

from djangogramm.models import Post, Comment, Image

fake = Faker()
CustomUser = get_user_model()


def create_user(num_users):
    users = []
    for i in range(num_users):
        username = fake.user_name()
        email = fake.email()
        password = 'password'
        user = CustomUser.objects.create_user(username=username, email=email, password=password)
        users.append(user)
    return users


def get_random_photo_path(photo_folder: pathlib.Path = settings.MEDIA_ROOT):
    photo_files = os.listdir(photo_folder)
    return pathlib.Path(photo_folder) / random.choice(photo_files)


def create_posts_with_photos(users: list[CustomUser], posts_num: int, max_images_for_post: int = 3) -> list[Post]:
    posts = []
    for i in range(posts_num):
        author = random.choice(users)
        description = fake.text(max_nb_chars=100)
        post = Post.objects.create(author=author, description=description)
        num_images = random.randint(1, max_images_for_post)
        for _ in range(num_images):
            photo_path = get_random_photo_path()
            with open(photo_path, 'rb') as photo_file:
                image = Image(post=post)
                image.image.save(pathlib.Path(photo_path.name), File(photo_file))
        posts.append(post)
    return posts


def create_comments(users: list[CustomUser], posts: list[Post], comments_num: int) -> list[Comment]:
    comments = []
    for post in posts:
        for _ in range(comments_num):
            author = random.choice(users)
            text = fake.text(max_nb_chars=255)
            comment = Comment.objects.create(post=post, author=author, text=text)
            comments.append(comment)
    return comments


def create_likes(users: list[CustomUser], posts: list[Post], likes_num: int) -> None:
    for post in posts:
        for _ in range(likes_num):
            user = random.choice(users)
            if user not in post.likes.all():
                post.likes.add(user)


if __name__ == '__main__':
    users = create_user(5)
    posts = create_posts_with_photos(users, 10)
    comments = create_comments(users, posts, 10)
    create_likes(users, posts, likes_num=10)
