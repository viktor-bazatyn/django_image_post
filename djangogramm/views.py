from django.shortcuts import render, redirect

from djangogramm.forms import PostForm, ImageForm
from djangogramm.models import Post


def index(request):
    posts = Post.objects.prefetch_related('images').all()
    return render(request, 'djangogramm/index.html', {'posts': posts})


def post_detail(request, post_id: int):
    post = Post.objects.get(pk=post_id)
    return render(request, 'djangogramm/post_detail.html', {'post': post})


def create_post(request):
    if request.method == 'POST':
        post_form = PostForm(request.POST)
        image_form = ImageForm(request.POST, request.FILES)
        if post_form.is_valid() and image_form.is_valid():
            post = post_form.save(commit=False)
            post.author = request.user
            post.save()
            image = image_form.save(commit=False)
            image.post = post
            image.save()
            return redirect('djangoinsta:user_posts')
    else:
        post_form = PostForm()
        image_form = ImageForm()

    return render(request, 'djangogramm/create_post.html', {'post_form': post_form, 'image_form': image_form})


def user_posts(request):
    posts = Post.objects.filter(author=request.user).order_by('-created_at')
    return render(request, 'djangogramm/user_posts.html', {'posts': posts})
