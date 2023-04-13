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
    def is_stored_posts(self, request, post_id):
        stored_posts = request.session.get("stored_posts")
        if stored_posts is not None:
            is_saved_for_later = post_id in stored_posts
        else:
            is_saved_for_later = False

        return is_saved_for_later

    def get(self, request, slug):
        post = get_object_or_404(Post, slug=slug)
        
        context = {
            "post": post,
            "tags": post.tags.all(),
            "comment_form": CommentForm(),
            "comments": post.comments.all().order_by("-id"),
            "saved_for_later": self.is_stored_posts(request, post.id)
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
            "comments": post.comments.all().order_by("-id"),
            "saved_for_later": self.is_stored_posts(request, post.id)
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

class ReadLaterView(View):
    def get(self, request):
        stored_posts = request.session.get("stored_posts")

        context = {}

        if stored_posts is None or len(stored_posts) == 0:
            context["posts"] = []
            context["has_posts"] = False
        else:
            context["posts"] = Post.objects.filter(id__in=stored_posts)
            context["has_posts"] = True
        
        return render(request, "blog/stored_posts.html", context)

    def post(self, request):
        stored_posts = request.session.get("stored_posts")

        if stored_posts is None:
            stored_posts = []

        post_id = int(request.POST["post_id"])

        if post_id not in stored_posts:
            stored_posts.append(post_id)
        else:
            stored_posts.remove(post_id)
            
        request.session["stored_posts"] = stored_posts

        return HttpResponseRedirect("/")