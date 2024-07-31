from django.contrib.auth import login
from django.shortcuts import redirect, render, get_object_or_404
from users.forms import CustomUserCreationForm, AvatarForm
from .models import CustomUser
from djangogramm.models import Post, Subscriber
from django.contrib import messages


def home(request):
    return render(request, "users/home.html")


def dashboard(request):
    if not request.user.is_authenticated:
        return redirect('login')

    user = request.user
    user_posts = Post.objects.filter(author=user)
    subscribers = Subscriber.objects.filter(user=user).values_list('subscribed_to', flat=True)
    subscriber_posts = Post.objects.filter(author__in=subscribers)
    posts = user_posts | subscriber_posts
    posts = posts.order_by('-created_at')
    for post in posts:
        post.is_liked_by_user = post.is_liked_by(user)

    subscriber_count = Subscriber.objects.filter(subscribed_to=user).count()
    subscription_count = Subscriber.objects.filter(user=user).count()

    return render(request, "users/dashboard.html", {
        'user': user,
        'posts': posts,
        'subscriber_count': subscriber_count,
        'subscription_count': subscription_count,
    })


def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            if CustomUser.objects.filter(email=email).exists():
                messages.error(request, "A user with this email already exists.")
                return render(request, "users/register.html", {"form": form})
            else:
                user = form.save()
                login(request, user, backend='django.contrib.auth.backends.ModelBackend')
                return redirect('dashboard')
        else:
            return render(request, "users/register.html", {"form": form})
    else:
        # Retrieve social auth data from session
        social_auth_data = request.session.pop('social_auth_data', None)
        form = CustomUserCreationForm(social_auth_data=social_auth_data)
        return render(request, "users/register.html", {"form": form})


def add_avatar(request):
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
