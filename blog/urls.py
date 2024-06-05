from django.urls import path, include

from .views import (
    list_posts,
    post_detail,
)

urlpatterns = [
    path('posts/', list_posts, name='list_posts'),
    path('posts/<str:slug>/', post_detail, name='post_detail'),
]
