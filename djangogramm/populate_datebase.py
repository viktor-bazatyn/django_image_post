import os
import django
from faker import Faker
import random
from django.core.files import File

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "base.settings")

django.setup()

from djangogramm.models import User, Post, Comment, Like

fake = Faker()


def create_user(num_users):
    users = []
    for i in range(num_users):
        username = fake.user_name()
        email = fake.email()
        password = 'password'
        user = User.objects.create_user(username=username, email=email, password=password)
        users.append(user)
    return users


def get_random_photo_path():
    photo_folder = "static/images"
    photo_files = os.listdir(photo_folder)
    return os.path.join(photo_folder, random.choice(photo_files))


def create_posts_with_photos(users, num_posts):
    posts = []
    for i in range(num_posts):
        author = random.choice(users)
        description = fake.text(max_nb_chars=100)
        post = Post.objects.create(author=author, description=description)
        photo_path = get_random_photo_path()
        with open(photo_path, 'rb') as photo_file:
            post.image.save(os.path.basename(photo_path), File(photo_file))
        posts.append(post)
    return posts


def create_comments(users, posts, num_comments):
    comments = []
    for post in posts:
        for _ in range(num_comments):
            author = random.choice(users)
            text = fake.text()
            comment = Comment.objects.create(post=post, author=author, text=text)
            comments.append(comment)
    return comments


def create_likes(users, posts, num_likes):
    likes = []
    for post in posts:
        for _ in range(num_likes):
            user = random.choice(users)
            like = Like.objects.create(post=post, user=user)
            likes.append(like)
    return likes


if __name__ == '__main__':
    users = create_user(1)
    posts = create_posts_with_photos(users, 10)
    comments = create_comments(users, posts, 10)
    likes = create_likes(users, posts, 10)
