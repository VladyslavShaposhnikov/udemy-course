from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('posts', views.PostsListView.as_view(), name='posts'),
    path('posts/<slug:slug>', views.PostDetailView.as_view(), name='post-detail'),
    path('tag/<str:tag>', views.TagPostsView.as_view(), name='tag-posts'),
    path("read-later", views.ReadLaterView.as_view(), name="read-later")
]