from email.policy import default
from django.db import models
from ckeditor.fields import RichTextField


class Publisher(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    age = models.IntegerField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}"

class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.name}"

class Article(models.Model):
    title = models.CharField(max_length=100)
    short_content = models.CharField(max_length=180)
    content = RichTextField()
    image = models.ImageField(upload_to="articles", null=True, blank=True)
    author = models.ForeignKey(Publisher, on_delete=models.DO_NOTHING)
    is_headline= models.BooleanField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    date_published = models.DateTimeField()
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, default=1)




