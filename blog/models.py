from django.db import models
from django.core.validators import MinLengthValidator


class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Posts(models.Model):
    title = models.CharField(max_length=90)
    excerpt = models.CharField(max_length=150)
    image_name = models.CharField(max_length=90)
    date = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True)
    content = models.TextField(validators=[MinLengthValidator(10)])
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, related_name='posts')
    
    def __str__(self):
        return f"{self.title}, {self.date}"
    
class Tag(models.Model):
    post = models.ManyToManyField(Posts)
    caption = models.CharField(max_length=90)

    def __str__(self):
        return f"{self.caption}"