from django.db import models

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
    
    class Meta:
        ordering = ['-created_on']