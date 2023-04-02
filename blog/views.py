from django.views.generic import ListView
from django.views import View
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import get_object_or_404, render

from .models import Post
from .forms import CommentForm


class IndexView(ListView):
    template_name = "blog/index.html"
    model = Post
    ordering = ["-date"]
    context_object_name = "posts"

    def get_queryset(self):
        queryset = super().get_queryset()
        data = queryset[:3]
        return data

class PostsListView(ListView):
    template_name = "blog/all_posts.html"
    model = Post
    ordering = ["-date"]
    context_object_name = "all_posts"

class PostDetailView(View):
    template_name = "blog/post_detail.html"
    model = Post

    def get(self, request, slug):
        post = get_object_or_404(Post, slug=slug)
        context = {
            "post": post,
            "tags": post.tags.all(),
            "comment_form": CommentForm(),
            "comments": post.comments.all().order_by("-id")
        }
        return render(request, "blog/post_detail.html", context)
    
    def post(self, request, slug):
        comment_form = CommentForm(request.POST)
        post = get_object_or_404(Post, slug=slug)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
            return HttpResponseRedirect(reverse("post-detail", args=[slug]))
        
        post = get_object_or_404(Post, slug=slug)
        context = {
            "post": post,
            "tags": post.tags.all(),
            "comment_form": comment_form,
            "comments": post.comments.all().order_by("-id")
        }
        return render(request, "blog/post_detail.html", context)


class TagPostsView(ListView):
    template_name = "blog/tag_posts.html"
    model = Post
    context_object_name = "posts"

    def get_queryset(self):
        return Post.objects.filter(tags__caption=self.kwargs['tag'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tag"] = self.kwargs['tag']
        return context