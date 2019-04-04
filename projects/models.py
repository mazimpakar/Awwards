from django.db import models
import datetime as dt
from django.contrib.auth.models import User
from tinymce.models import HTMLField
# Create your models here.

class Profile(models.Model):
    username = models.CharField(default='User',max_length=80)
    picture = models.ImageField(upload_to='images/', blank=True)
    bio = HTMLField()
    # projects = models.ForeignKey(User,null=True)
    name = models.CharField(max_length=30)
    user = models.ForeignKey(User,null=True)

    def __str__(self):
        return self.name

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    @classmethod
    def get_profiles(cls):
        profiles = cls.objects.all()
        return profiles
   
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
    
           

class Project(models.Model):
    image = models.ImageField(upload_to='images/', blank=True)
    title = models.CharField(max_length =30 )
    description = models.TextField(null = True)
    links = models.URLField(blank=True)
    user = models.ForeignKey(User,null=True)
    
    def __str__(self):
        return self.title

    def save_images(self):
        self.save()   

    def delete_images(self):
    	self.delete()
    @classmethod
    def all_images(cls):
        images = cls.objects.all()
        return images

    @classmethod
    def get_images(cls, id):
        images = cls.objects.get(id=id)
        return image
    
   
    @classmethod
    def search_by_title(cls,search_term):
        projects = cls.objects.filter(title__icontains=search_term)
        return projects
