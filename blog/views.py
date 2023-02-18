from django.shortcuts import render, HttpResponse
from .models import Post, Author, Tag
from django.shortcuts import  get_object_or_404


all_posts = Post.objects.all()

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
    identified_post = get_object_or_404(Post, slug=slug)
    author = Author.objects.get(post=identified_post)
    tags = Tag.objects.filter(post=identified_post)
    #identified_post = next(post for post in all_posts if post['slug'] == slug)
    return HttpResponse(render(request, 'blog/post_detail.html', {
        'post': identified_post,
        'author': author,
        'tags': tags,
    }))

def tag_posts(request, tag):
    tags = get_object_or_404(Tag, caption=tag)
    all_posts = tags.post.all()
    return HttpResponse(render(request, 'blog/tag_posts.html', {
        'tag_posts': tags,
        'posts': all_posts,
    }))