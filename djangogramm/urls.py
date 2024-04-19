from django.urls import path
from . import views

urlpatterns = [
    path('profile/<int:user_id>', views.view_profile, name='view-profile'),
    path('profile/edit/', views.edit_profile, name='edit-profile'),
    path('posts/', views.post_list, name='post-list'),
    path('posts/create/', views.create_new_post, name='create-post'),
    path('posts/<int:post_id>/like/', views.like_post, name='like-post'),
    path('posts/<int:post_id>/comment/', views.add_comment, name='add-comment'),
]