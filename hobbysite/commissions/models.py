from django.db import models
from django.urls import reverse

class Commission(models.Model):
    title = models.CharField(max_length = 255)
    description = models.TextField(blank = False)
    people_required = models.PositiveBigIntegerField()
    created_on = models.DateTimeField(auto_now_add = True)
    updated_on = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['created_on']

class Comment(models.Model):
    commission = models.ForeignKey(Commission, on_delete = models.CASCADE)
    entry = models.TextField(blank = False)
    created_on = models.DateTimeField(auto_now_add = True)
    updated_on = models.DateTimeField(auto_now = True)

    def get_absolute_url(self):
        return reverse('commissions:comment_detail', args=[str(self.pk)])
    
    class Meta:
        ordering = ['-created_on']