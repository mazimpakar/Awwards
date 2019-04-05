from django.test import TestCase
from .models import Project,Profile,Rating

class ProjectTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.rose= Project()
    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.rose,Project))

    # Testing Save Method
    def test_save_method(self):
        self.rose.save_project()
        description= Project.objects.all()
        self.assertTrue(len(description) > 0)

    # def test_all_projets(self):
    #     self.rose.all_projects()
    #     title=Project.objects.all()
    #     self.assertTrue(len(title) > 0)
        

  
       
class RatingTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.rose= Rating()
    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.rose,Rating))

   
class ProfileTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.rose= Profile( )
    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.rose,Profile))

    # Testing Save Method
    def test_save_method(self):
        self.rose.save_profile()
        image = Profile.objects.all()
        self.assertTrue(len(image) > 0) 
    
