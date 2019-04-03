from django import forms
from .models import Project,Profile

class NewProjectsForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ['user', 'pub_date']
        widgets = {
            'profile': forms.CheckboxSelectMultiple(),
        }  
class ProfileForm(forms.ModelForm):
	model = Profile
	username = forms.CharField(label='Username',max_length = 30)
	
	bio = forms.CharField(label='Image Title',max_length=500)
	projects = forms.CharField(max_length =30)        