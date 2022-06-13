from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Project , Ratings, Profile


class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields =['username', 'email', 'password1', 'password2']
        
        
class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'url','location','description', 'image']
        
        
class RatingsForm(ModelForm):
    class Meta:
        model = Ratings
        fields = ['design', 'usability', 'content']    
        

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['fullname','email','bio','profile_pic']
        
class SearchForm(forms.Form):
    name = forms.CharField(max_length=100)
    