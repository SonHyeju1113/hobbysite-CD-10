from django.db import models
from django.urls import reverse

class ArticleCategory(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=False)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name']

class Article(models.Model):
    title = models.CharField(max_length=255)
    category = models.ForeignKey(ArticleCategory, on_delete=models.SET_NULL, null=True, related_name="category")
    entry = models.TextField(blank=False)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('article_detail', args=[str(self.pk)])
    
    class Meta:
        ordering = ['-created_on']
