from django.contrib.auth import login
from django.shortcuts import redirect, render
from users.forms import CustomUserCreationForm, AvatarForm
from .models import CustomUser

def dashboard(request):
    avatars = CustomUser.objects.filter
    return render(request, "users/dashboard.html", {'avatars': avatars})


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
        avatar_form = AvatarForm(request.POST, request.FILES)
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