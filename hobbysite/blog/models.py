from django.db import models

class ArticleCategory(models.Model):
    name = models.CharField(max_Length=255)
    description = models.TextField(blank=False)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name']
