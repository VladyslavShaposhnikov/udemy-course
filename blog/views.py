from django.shortcuts import render, HttpResponse
from django.http import request

post_list = {
    'post 1': 'Thats my first post',
    'post 2': 'Thats my second post',
    'post 3': 'Thats my thirth post',
    'post 4': 'Thats my forth post',
}

def index(request):
    return HttpResponse(render(request, 'blog/index.html'))

def posts(request):
    return HttpResponse(render(request, 'blog/all_posts.html'))

def post_detail(request, slug):
    #post = slug
    return HttpResponse(render(request, 'blog/post_detail.html'))