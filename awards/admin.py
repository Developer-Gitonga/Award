from django.contrib import admin
from .models import Project, Ratings, Profile
# Register your models here.

admin.site.register(Project)
admin.site.register(Profile)
admin.site.register(Ratings)
