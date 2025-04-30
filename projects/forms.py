from django import forms
from .models import Project, AboutMe

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'link']
        
class AboutMeForm(forms.ModelForm):
    class Meta:
        model = AboutMe
        fields = ['name', 'bio', 'skills', 'contact_info', 'photo']