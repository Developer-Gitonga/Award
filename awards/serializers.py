from rest_framework import serializers
from . models import Profile, Project


class ProfilesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['fullname','email','bio', 'profile_pic']
        
class ProjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['title','url','location','description']