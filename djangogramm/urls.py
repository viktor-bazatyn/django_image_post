from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('post/<uuid:post_id>/', views.post_detail, name='post_detail'),
    path('user_posts/', views.user_posts, name='user_posts'),
    path('create_post/', views.create_post, name='create_post'),
]
app_name = 'djangoinsta'

