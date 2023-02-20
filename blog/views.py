from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import Post


def index(request):
    latest_posts = Post.objects.all().order_by('-date')[:3]
    return HttpResponse(render(request, 'blog/index.html', context={
        'posts': latest_posts
    }))

def posts(request):
    all_posts = Post.objects.all().order_by("-date")
    return HttpResponse(render(request, 'blog/all_posts.html', {
        'all_posts': all_posts,
    }))

def post_detail(request, slug):
    identified_post = get_object_or_404(Post, slug=slug)
    author = identified_post.author
    tags = identified_post.tags.all()
    return HttpResponse(render(request, 'blog/post_detail.html', {
        'post': identified_post,
        'author': author,
        'tags': tags,
    }))

def tag_posts(request, tag):
    all_posts = Post.objects.filter(tags__caption=tag)
    return HttpResponse(render(request, 'blog/tag_posts.html', {
        'posts': all_posts,
        'tag': tag
    }))