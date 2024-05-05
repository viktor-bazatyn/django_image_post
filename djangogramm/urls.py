from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('post/<uuid:post_id>/', views.post_detail, name='post_detail'),
]
app_name = 'djangoinsta'
