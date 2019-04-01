from django.db import models
import datetime as dt
from django.contrib.auth.models import User
from tinymce.models import HTMLField
# Create your models here.

class Profile(models.Model):
    picture = models.ImageField(upload_to='images/', blank=True)
    bio = models.CharField(max_length =30)
    projects = models.CharField(max_length =30)
    contacts = models.CharField(max_length =30)
    user = models.ForeignKey(User,null=True)

    def __str__(self):
        return self.bio
class tags(models.Model):
    name = models.CharField(max_length =30)
    def __str__(self):
        return self.name 
class Ratings(models.Model):
    # image = models.ImageField(upload_to='images/', blank=True)
    user = models.ForeignKey(User,null=True)
    design = models.CharField(max_length =30 )
    usability = models.TextField(null = True)
    contents = models.CharField(max_length =30)
    
           

class Projects(models.Model):
    image = models.ImageField(upload_to='images/', blank=True)
    title = models.CharField(max_length =30 )
    description = models.TextField(null = True)
    links = models.URLField(blank=True)
    user = models.ForeignKey(User,null=True)
    
    def __str__(self):
        return self.name

    def save_projects(self):
        self.save()   

    def delete_projects(self):
    	self.delete()
    @classmethod
    def all_projects(cls):
        projects = cls.objects.all()
        return projects

    @classmethod
    def get_projects(cls, id):
        projects = cls.objects.get(id=id)
        return project
    def __str__(self):
    	return self.user.username
   
    @classmethod
    def search_by_title(cls,search_term):
        projects = cls.objects.filter(title__icontains=search_term)
        return projects
