from django.contrib.auth import login
from django.shortcuts import redirect, render, get_object_or_404
from users.forms import CustomUserCreationForm, AvatarForm
from .models import CustomUser
from djangogramm.models import Post, Subscriber


def dashboard(request):
    user = request.user

    # Отримати всі пости користувача
    user_posts = Post.objects.filter(author=user)

    # Отримати пости підписників
    subscribers = Subscriber.objects.filter(user=user).values_list('subscribed_to', flat=True)
    subscriber_posts = Post.objects.filter(author__in=subscribers)

    # Об'єднати пости
    posts = user_posts | subscriber_posts

    # Додати атрибут is_liked_by_user до кожного поста
    for post in posts:
        post.is_liked_by_user = post.is_liked_by(user)

    # Обчислити кількість підписників і підписок
    subscriber_count = Subscriber.objects.filter(subscribed_to=user).count()
    subscription_count = Subscriber.objects.filter(user=user).count()

    return render(request, "users/dashboard.html", {
        'user': user,
        'posts': posts,
        'subscriber_count': subscriber_count,
        'subscription_count': subscription_count,
    })


def register(request):
    if request.method == "GET":
        form = CustomUserCreationForm()
        return render(request, "users/register.html", {"form": form})
    elif request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return render(request, "users/dashboard.html")
        else:
            return render(request, "users/register.html", {"form": form})
    else:
        return render(request, "users/register.html", {"form": CustomUserCreationForm()})


def add_avatar(request):
    if request.method == "POST":
        if request.method == "POST":
            form = AvatarForm(request.POST, request.FILES, instance=request.user)
            if form.is_valid():
                user = form.save(commit=False)
                user.avatar = form.cleaned_data['avatar']
                user.save(update_fields=['avatar'])
        return redirect('dashboard')
    else:
        avatar_form = AvatarForm()
    return render(request, "users/add_avatar.html", {"avatar_form": avatar_form})


def subscribe(request, user_id):
    user_to_subscribe = get_object_or_404(CustomUser, id=user_id)
    if not Subscriber.objects.filter(user=request.user, subscribed_to=user_to_subscribe).exists():
        Subscriber.objects.create(user=request.user, subscribed_to=user_to_subscribe)
    return redirect('dashboard')