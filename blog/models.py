from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from ckeditor.fields import RichTextField

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = RichTextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    summary = models.TextField()
    featured_image = models.ImageField(upload_to='featured_images/', null=True, blank=True)
    status = models.CharField(max_length=255, choices=[('draft', 'Draft'), ('published', 'Published')])
    created_at = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True, max_length=255) # SEO Url

    class Meta:
        ordering = ['-published_date']

    def __str__(self):
        return self.title

    def publish(self):
        self.published_date = timezone.now()
        self.save()


class Comment(models.Model):
    text = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    is_approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']
    