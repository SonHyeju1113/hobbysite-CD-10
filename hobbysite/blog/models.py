"""
@brief Models for Blog app.
"""
from django.db import models
from django.urls import reverse

class ArticleCategory(models.Model):
    """
    @brief Instantiates ArticleCategory model.
    """
    name = models.CharField(max_length=255)
    description = models.TextField(blank=False)

    def __str__(self):
        return self.name

    class Meta:
        """
        @brief To sort the model in ascending order with respect to model name.
        """
        ordering = ['name']

class Article(models.Model):
    """
    @brief Instantiates Article model.
    """
    title = models.CharField(max_length=255)
    category = models.ForeignKey(ArticleCategory,
                                 on_delete=models.SET_NULL,
                                 null=True,
                                 related_name="category")
    entry = models.TextField(blank=False)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """
        @brief returns the specific URL for viewing the current 
        instance with primary key as argument.
        """
        return reverse('article_detail', args=[str(self.pk)])

    class Meta:
        """
        @brief To sort the model in descending order with respect to date created.
        """
        ordering = ['-created_on']
