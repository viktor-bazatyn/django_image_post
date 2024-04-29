from django.urls import path
from . import views

urlpatterns = [
    path('profile/edit/', views.main, name='main'),
    path('posts/', views.post_list, name='post-list'),
    path('posts/create/', views.create_new_post, name='create-post'),
    path('posts/<int:post_id>/like/', views.like_post, name='like-post'),
    path('posts/<int:post_id>/comment/', views.add_comment, name='add-comment'),
]