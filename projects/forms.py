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
	class Meta:
		model = Profile
		
		exclude = ['user']       