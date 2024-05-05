from django.shortcuts import render

from djangogramm.models import Post


def index(request):
    posts = Post.objects.all()
    return render(request, 'djangogramm/index.html', {'posts': posts})


def post_detail(request, post_id: int):
    post = Post.objects.get(pk=post_id)
    return render(request, 'djangogramm/post_detail.html', {'post': post})
