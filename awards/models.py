from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fullname = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    bio = models.TextField(max_length=500, blank=True)
    profile_pic = CloudinaryField('image')
    
    def __str__(self):
        return self.user.username


class Project(models.Model):
    title = models.CharField(max_length=150)
    url = models.URLField()
    location = models.CharField(max_length=100)
    description = models.TextField()
    image = CloudinaryField('image')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='projects')
    
    class Meta:
        ordering = ['-created', '-updated']
    
    def __str__(self):
        return self.title
    
    def designcount(self):
        return self.ratings.all.design
    
    def num_of_ratings(self):
        return self.ratings.count()
    
    def average_of_all_ratings(self):
        return "{:.1f}".format((float(self.average_of_design_ratings())+float(self.average_of_usability_ratings())+float(self.average_of_content_ratings()))/3)
    
    def average_of_design_ratings(self):
        return "{:.1f}".format(self.ratings.aggregate(models.Avg('design'))['design__avg'] or 0)
    
    def average_of_usability_ratings(self):
        return "{:.1f}".format(self.ratings.aggregate(models.Avg('usability'))['usability__avg'] or 0)

    
    def average_of_content_ratings(self):
        return "{:.1f}".format(self.ratings.aggregate(models.Avg('content'))['content__avg'] or 0)

    
    
class Ratings(models.Model):
    design = models.IntegerField(default=0)
    usability = models.IntegerField(default=0)
    content = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='users')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='ratings')
    
    def __str__(self):
        return str(self.average_rating())
    
    def average_rating(self):
        return '{:.1f}'.format((self.design + self.usability + self.content)/3)
    