from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('ajax/load_posts/', views.load_posts, name='load_posts'),
    path('post/<uuid:post_id>/', views.post_detail, name='post_detail'),
    path('user/<str:username>/', views.user_profile, name='user_profile'),
    path('user_posts/', views.user_posts, name='user_posts'),
    path('create_post/', views.create_post, name='create_post'),
    path('user/<str:username>/subscribe/', views.subscribe, name='subscribe'),
    path('user/<str:username>/unsubscribe/', views.unsubscribe, name='unsubscribe'),
    path('user/<str:username>/subscribers/', views.subscribers_list, name='subscribers_list'),
    path('user/<str:username>/subscriptions/', views.subscriptions_list, name='subscriptions_list'),
    path('post/<uuid:post_id>/like_unlike_post/', views.like_unlike_post, name='like_unlike_post'),
]
app_name = 'djangoinsta'