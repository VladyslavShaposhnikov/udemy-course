from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('posts', views.posts, name='posts'),
    path('posts/<slug:slug>', views.post_detail, name='post-detail'),
    path('tag/<str:tag>', views.tag_posts, name='tag-posts'),
]