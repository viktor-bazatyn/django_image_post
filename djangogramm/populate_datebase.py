import os
import django
from faker import Faker
import random
from models import User, Post, Comment, Like

fake = Faker()

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "base.settings")
django.setup()


def create_user(num_users):
    users = []
    for i in range(num_users):
        username = fake.user_name()
        email = fake.email()
        password = 'password'
        user = User.objects.create_user(username=username, email=email, password=password)
        users.append(user)
    return users


def create_posts(users, num_posts):
    posts = []
    for i in range(num_posts):
        author = random.choice(users)
        description = fake.text(max_nb_chars=100)
        post = Post(author=author, description=description)
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
    posts = create_posts(users, 10)
    comments = create_comments(users, posts, 10)
    likes = create_likes(users, posts, 10)
