from .models import Post
from django.views.generic import ListView, DetailView


class IndexView(ListView):
    template_name = "blog/index.html"
    model = Post
    ordering = ["-date"]
    context_object_name = "posts"

    def get_queryset(self):
        queryset = super().get_queryset()
        data = queryset[:3]
        return data

class PostsView(ListView):
    template_name = "blog/all_posts.html"
    model = Post
    ordering = ["-date"]
    context_object_name = "all_posts"

class PostDetailView(DetailView):
    template_name = "blog/post_detail.html"
    model = Post
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tags"] = self.object.tags.all()
        return context

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