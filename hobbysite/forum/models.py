from user_management.models import Profile
from django.db import models
from django.urls import reverse

class ThreadCategory(models.Model):
    name = models.CharField(max_length = 255)
    description = models.TextField(blank = False)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name']

class Thread(models.Model):
    title = models.CharField(max_length = 255)
    author = models.ForeignKey(Profile, on_delete = models.SET_NULL, null = True, related_name = "author")
    category = models.ForeignKey(PostCategory, on_delete = models.SET_NULL, null = True, related_name = "category")
    entry = models.TextField(blank = False)
    created_on = models.DateTimeField(auto_now_add = True)
    updated_on = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('forum:post_detail', args = [str(self.pk)])

    class Meta:
        ordering = ['-created_on']

