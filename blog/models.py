from django.db import models
from datetime import datetime


class Posts(models.Model):
    title = models.CharField(max_length=90)
    excerpt = models.CharField(max_length=150)
    image_name = models.CharField(max_length=90)
    date = models.DateTimeField(auto_now=True)
    slug = models.SlugField()
    content = models.TextField()
    
    def __str__(self):
        return f"{self.title}, {self.date}"
    
class Author(models.Model):
    post = models.ForeignKey(Posts, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class Tag(models.Model):
    post = models.ManyToManyField(Posts)
    caption = models.CharField(max_length=90)

    def __str__(self):
        return f"{self.caption}"