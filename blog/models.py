from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from ckeditor.fields import RichTextField

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = RichTextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    summary = models.TextField(max_length=255)
    featured_image = models.ImageField(upload_to='featured_images/', null=False)
    status = models.CharField(max_length=255, choices=[('draft', 'Draft'), ('published', 'Published')])
    # categories = models.ManyToManyField(Category, through='PostCategory')
    # tags = models.ManyToManyField(Tag, through='PostTag') 
    created_at = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True, max_length=255) # SEO Url

    class Meta:
        ordering = ['-published_date']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.status == 'published' and not self.published_date:
            self.published_date = timezone.now()
        super().save(*args, **kwargs)
        


class Comment(models.Model):
    text = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    is_approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']


# class Category(models.Model):
#     name = models.CharField(max_length=255)
#     description = models.TextField()

#     def __str__(self):
#         return self.name

# class Tag(models.Model):
#     name = models.CharField(max_length=255)

#     def __str__(self):
#         return self.name

# class PostCategory(models.Model):
#     post = models.ForeignKey(Post, on_delete=models.CASCADE)
#     category = models.ForeignKey(Category, on_delete=models.CASCADE)

#     def __str__(self):
#         return f"{self.post.title} - {self.category.name}"

# class PostTag(models.Model):
#     post = models.ForeignKey(Post, on_delete=models.CASCADE)
#     tag = models.ForeignKey(Tag, on_delete=models.CASCADE)

#     def __str__(self):
#         return f"{self.post.title} - {self.tag.name}"
    