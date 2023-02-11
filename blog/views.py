from django.shortcuts import render, HttpResponse
from .models import Posts, Author, Tag


all_posts = Posts.objects.all()

def index(request):
    sorted_posts = all_posts.order_by('date')
    latest_posts = sorted_posts[:3]
    return HttpResponse(render(request, 'blog/index.html', context={
        'posts': latest_posts
    }))

def posts(request):
    return HttpResponse(render(request, 'blog/all_posts.html', {
        'all_posts': all_posts,
    }))

def post_detail(request, slug):
    identified_post = next(post for post in all_posts if post['slug'] == slug)
    return HttpResponse(render(request, 'blog/post_detail.html', {
        'post': identified_post,
    }))