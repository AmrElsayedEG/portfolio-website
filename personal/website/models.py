from django.db import models

# Create your models here.

class projects(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    is_live = models.BooleanField(default=False)
    primary_img = models.ImageField(upload_to='imgs')
    secondary_img = models.ImageField(upload_to='imgs')
    project_description = models.TextField()
    technologies_used = models.TextField()
    project_url = models.URLField(default='https://github.com/AmrElsayedEG/')

    def __str__(self):
        return self.name