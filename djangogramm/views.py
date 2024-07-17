from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from djangogramm.forms import PostForm, ImageForm
from djangogramm.models import Post, Subscriber
from users.models import CustomUser
from django.template.loader import render_to_string
from django.core.paginator import Paginator


def index(request):
    user = request.user
    posts = Post.objects.all().order_by('-created_at')
    paginator = Paginator(posts, 10)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)

    for post in page_obj:
        post.is_liked_by_user = post.is_liked_by(user)

    return render(request, "djangogramm/index.html", {
        'user': user,
        'posts': page_obj,
    })


def load_posts(request):
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        page_number = int(request.GET.get('page', 1))
        posts = Post.objects.all().order_by('-created_at')
        paginator = Paginator(posts, 10)
        page_obj = paginator.get_page(page_number)

        for post in page_obj:
            post.is_liked_by_user = post.is_liked_by(request.user)

        has_more = page_obj.has_next()

        html = render_to_string('djangogramm/posts.html', {'posts': page_obj, 'user': request.user})
        if has_more:
            load_more_button = '<div class="col-md-7 mx-auto text-center"><button id="load-more" class="btn btn-primary">Load More</button></div>'
            html += load_more_button

        return HttpResponse(html)

    return HttpResponse('Invalid request', status=400)


def like_unlike_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    user = request.user

    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'like':
            post.like(user)
        elif action == 'unlike':
            post.unlike(user)

    return redirect(request.META.get('HTTP_REFERER', 'index'))


def post_detail(request, post_id):
    user = request.user
    post = get_object_or_404(Post, id=post_id)
    post.is_liked_by_user = post.is_liked_by(user)

    return render(request, "djangogramm/post_detail.html", {
        'user': user,
        'post': post,
    })


def create_post(request):
    if request.method == 'POST':
        post_form = PostForm(request.POST)
        image_form = ImageForm(request.POST, request.FILES)

        if post_form.is_valid() and (not request.FILES or image_form.is_valid()):
            post = post_form.save(commit=False)
            post.author = request.user
            post.save()

            if request.FILES:
                image = image_form.save(commit=False)
                image.post = post
                image.save()

            return redirect('dashboard')
    else:
        post_form = PostForm()
        image_form = ImageForm()

    return render(request, 'djangogramm/create_post.html', {'post_form': post_form, 'image_form': image_form})


def user_posts(request):
    posts = Post.objects.filter(author=request.user).order_by('-created_at')
    return render(request, 'djangogramm/user_posts.html', {'posts': posts})


def subscribers_list(request, username):
    user_profile = get_object_or_404(CustomUser, username=username)
    subscribers = user_profile.subscribers.all()
    return render(request, 'djangogramm/subscribers_list.html',
                  {'user_profile': user_profile, 'subscribers': subscribers})


def subscriptions_list(request, username):
    user_profile = get_object_or_404(CustomUser, username=username)
    subscriptions = user_profile.subscriptions.all()
    return render(request, 'djangogramm/subscriptions_list.html',
                  {'user_profile': user_profile, 'subscriptions': subscriptions})


def user_profile(request, username):
    user_profile = get_object_or_404(CustomUser, username=username)
    posts = Post.objects.filter(author=user_profile)
    for post in posts:
        post.is_liked_by_user = post.is_liked_by(request.user)
    subscriber_count = Subscriber.objects.filter(subscribed_to=user_profile).count()
    subscription_count = Subscriber.objects.filter(user=user_profile).count()
    is_subscribed = Subscriber.objects.filter(user=request.user, subscribed_to=user_profile).exists()
    return render(request, "djangogramm/user_profile.html", {
        'user_profile': user_profile,
        'posts': posts,
        'subscriber_count': subscriber_count,
        'subscription_count': subscription_count,
        'is_subscribed': is_subscribed,
    })


def subscribe(request, username):
    user_to_subscribe = get_object_or_404(CustomUser, username=username)
    if user_to_subscribe != request.user:
        if not Subscriber.objects.filter(user=request.user, subscribed_to=user_to_subscribe).exists():
            Subscriber.objects.create(user=request.user, subscribed_to=user_to_subscribe)
    return redirect('djangoinsta:user_profile', username=username)


def unsubscribe(request, username):
    user_to_unsubscribe = get_object_or_404(CustomUser, username=username)
    Subscriber.objects.filter(user=request.user, subscribed_to=user_to_unsubscribe).delete()
    return redirect('djangoinsta:user_profile', username=username)
