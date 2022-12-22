from django.shortcuts import render, HttpResponse
from datetime import date

all_posts = [
    {
    'slug': 'hike-in-the-mountains',
    'image': 'img2.jpg',
    'author': 'Vlad',
    'date': date(2022, 12, 17),
    'title': 'Mountain Hiking',
    'excerpt': "There is nothing like the views you get when hiking in the mountains! And I wasn't even prepared for what happend whilst I was enjoying the view!",
    'content': """
    Lorem ipsum dolor sit amet consectetur adipisicing elit. Nam voluptatum, ipsam accusantium quas, reiciendis corporis enim optio sit consequuntur culpa blanditiis cum doloribus. Voluptates praesentium aspernatur ipsum molestiae sequi voluptate.

    Lorem ipsum dolor sit amet consectetur adipisicing elit. Nam voluptatum, ipsam accusantium quas, reiciendis corporis enim optio sit consequuntur culpa blanditiis cum doloribus. Voluptates praesentium aspernatur ipsum molestiae sequi voluptate.

    Lorem ipsum dolor sit amet consectetur adipisicing elit. Nam voluptatum, ipsam accusantium quas, reiciendis corporis enim optio sit consequuntur culpa blanditiis cum doloribus. Voluptates praesentium aspernatur ipsum molestiae sequi voluptate.

    Lorem ipsum dolor sit amet consectetur adipisicing elit. Nam voluptatum, ipsam accusantium quas, reiciendis corporis enim optio sit consequuntur culpa blanditiis cum doloribus. Voluptates praesentium aspernatur ipsum molestiae sequi voluptate.
    """
    },
    {
    'slug': 'programming-is-fun',
    'image': 'me.jpg',
    'author': 'Vlad',
    'date': date(2022, 12, 29),
    'title': 'Programming and me',
    'excerpt': "Programming is fun, but it is more funniest whan you get paid for it",
    'content': """
    Lorem ipsum dolor sit amet consectetur adipisicing elit. Nam voluptatum, ipsam accusantium quas, reiciendis corporis enim optio sit consequuntur culpa blanditiis cum doloribus. Voluptates praesentium aspernatur ipsum molestiae sequi voluptate.

    Lorem ipsum dolor sit amet consectetur adipisicing elit. Nam voluptatum, ipsam accusantium quas, reiciendis corporis enim optio sit consequuntur culpa blanditiis cum doloribus. Voluptates praesentium aspernatur ipsum molestiae sequi voluptate.

    Lorem ipsum dolor sit amet consectetur adipisicing elit. Nam voluptatum, ipsam accusantium quas, reiciendis corporis enim optio sit consequuntur culpa blanditiis cum doloribus. Voluptates praesentium aspernatur ipsum molestiae sequi voluptate.

    Lorem ipsum dolor sit amet consectetur adipisicing elit. Nam voluptatum, ipsam accusantium quas, reiciendis corporis enim optio sit consequuntur culpa blanditiis cum doloribus. Voluptates praesentium aspernatur ipsum molestiae sequi voluptate.
    """
    }
]

def get_date(post):
    return post['date']

def index(request):
    sorted_posts = sorted(all_posts, key=get_date)
    latest_posts = sorted_posts[-3:]
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