from django.db import models
from django.urls import reverse

# Create your models here.
class ArticleCategory(models.Model):
    name = models.CharField(max_length=255)
    
    description = models.TextField(blank=False, default="")

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

class Article(models.Model):
    title = models.CharField(max_length=255)

    category = models.ForeignKey(ArticleCategory, on_delete=models.SET_NULL, null=True, related_name='article', limit_choices_to={"is_staff": True},)

    entry = models.TextField(blank=False, default="")

    header_image = models.ImageField(upload_to='images/', null=False, default='')

    created_on = models.DateTimeField(auto_now_add=True)

    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('wiki:article_detail', args=[str(self.pk)])

    class Meta:
        ordering = ['-created_on']

class Comment(models.Model):
    author = models.ForeignKey('user_management.Profile', on_delete=models.SET_NULL, null=True)

    article = models.ForeignKey(Article, on_delete=models.CASCADE)

    entry = models.TextField(blank=False, default="")

    created_on = models.DateTimeField(auto_now_add=True)

    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_on']