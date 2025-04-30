from django.db import models
from django.contrib.auth.models import User

#Adding a project model

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    link = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    
class AboutMe(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    skills = models.TextField()
    photo = models.ImageField(upload_to='about_me_photos/')
    contact_info = models.TextField()
    
    def __str__(self):
        return self.name