from django.shortcuts import render


def view_profile(request, user_id):
    user = "Alex"
    posts = "There is my posts"
    return render(request, 'view_profile.html', {'user': user, 'posts': posts})


def edit_profile(request):
    return render(request, 'edit_profile.html')


def post_list(request, posts):
    return render(request, 'post_list.html', {'posts': posts})


def create_new_post(request):
    return render(request, 'create_post.html')


def like_post(request, post_id):
    return render(request, 'like_post.html', {'post_id': post_id})


def add_comment(request, post_id):
    return render(request, 'add_comment.html', {'post_id': post_id})
