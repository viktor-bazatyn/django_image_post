from django.shortcuts import render


def register(request):
    return render(request, 'register.html')


def user_login(request):
    return render(request, 'login.html')


def user_logout(request):
    return render(request, 'logout.html')


def view_profile(request):
    return render(request, 'view_profile.html')


def edit_profile(request):
    return render(request, 'edit_profile.html')


def post_list(request):
    return render(request, 'post_list.html')


def create_new_post(request):
    return render(request, 'create_post.html')


def like_post(request):
    return render(request, 'like_post.html')


def add_comment(request):
    return render(request, 'add_comment.html')
