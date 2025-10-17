# projects/models.py
from django.db import models

class Technology(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Technologies"
class Project(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    featured_image = models.ImageField(upload_to='projects/')
    demo_link = models.URLField(blank=True)
    github_link = models.URLField(blank=True)
    technologies_used = models.ManyToManyField(Technology)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title