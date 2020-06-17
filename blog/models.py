from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from taggit.managers import TaggableManager


class Post(models.Model):


    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    tags=TaggableManager()
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='published')
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='blog_posts')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    status = models.CharField(
        max_length=10, choices=STATUS_CHOICES, default='draft')

    class Meta:
        ordering = ['-publish']

    def __str__(self):
        return f"{self.title} by {self.author}"


class Comment(models.Model):
    post=models.ForeignKey(Post,on_delete=models.CASCADE)
    body=models.TextField()

    author=models.ForeignKey(User,on_delete=models.CASCADE)
    commented_on=models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.author}'s comment"