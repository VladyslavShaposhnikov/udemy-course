from django.contrib import admin
from .models import Posts, Author, Tag

admin.register(Posts)
admin.register(Author)
admin.register(Tag)
