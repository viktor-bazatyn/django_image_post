from django.urls import path
from . import views

urlpatterns = [
    path('', views.register, name='register'),
    path('', views.user_login, name='login'),
    path('', views.user_logout, name='logout'),
    path('', views.view_profile, name='view-profile'),
    path('', views.edit_profile, name='edit-profile'),
    path('', views.post_list, name='post-list'),
    path('', views.create_new_post, name='create-post'),
    path('', views.like_post, name='like-post'),
    path('', views.add_comment, name='add-comment'),
]
