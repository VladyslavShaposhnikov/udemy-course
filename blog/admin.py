from django.contrib import admin
from .models import Posts, Author, Tag

admin.site.register(Author)
admin.site.register(Tag)
