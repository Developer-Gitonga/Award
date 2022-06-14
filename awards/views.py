from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ProjectsSerializer, ProfilesSerializer
from django.shortcuts import render,redirect
from django.contrib.auth import login
from .forms import RegisterForm,ProjectForm, RatingsForm, ProfileForm,SearchForm
from django.contrib.auth.models import User
from .models import Profile, Project, Ratings
# Create your views here.

def home(request):
    projects = Project.objects.all()
    main = Project.objects.get(id=1)
    form = ProjectForm()
    searchform = SearchForm()
    if request.method == 'POST':
        searchform = SearchForm(request.POST)
        if searchform.is_valid():
            name = searchform.cleaned_data['name']
            project = Project.objects.get(title=name)
            return redirect(f'project/{project.id}')
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            user = request.user
            title = form.cleaned_data['title']
            url = form.cleaned_data['url']
            location = form.cleaned_data['location']
            description = form.cleaned_data['description']
            image = form.cleaned_data['image']
            created_project = Project(title=title,url=url,location=location,description=description,image=image,user=user)
            created_project.save()
            return redirect('home')
    return render(request, 'ip3/index.html',{"title":"Home","projects":projects,"form":form,"searchform":searchform,"main":main})

def project(request, id):
    project = Project.objects.get(id=id)
    form = ProjectForm()
    ratingform = RatingsForm()
    searchform = SearchForm()

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            user = request.user
            title = form.cleaned_data['title']
            url = form.cleaned_data['url']
            location = form.cleaned_data['location']
            description = form.cleaned_data['description']
            image = form.cleaned_data['image']
            created_project = Project(title=title,url=url,location=location,description=description,image=image,user=user)
            created_project.save()
            return redirect('home')
    if request.method == 'POST':
        ratingform = RatingsForm(request.POST)
        if ratingform.is_valid():
            design = ratingform.cleaned_data['design']
            usability = ratingform.cleaned_data['usability']
            content = ratingform.cleaned_data['content']
            ratings = Ratings(design=design,usability=usability,content=content,user=request.user,project=project)
            ratings.save()
            
    if request.method == 'POST':
        searchform = SearchForm(request.POST)
        if searchform.is_valid():
            name = searchform.cleaned_data['name']
            project = Project.objects.get(title=name)
            return redirect(f'project/{project.id}')
    return render(request, 'ip3/single.html',{"title":"Single","project":project,"form":form,"ratingform":ratingform,"searchform":searchform})

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('home')
    else:
        form = RegisterForm()

    return render(request, 'registration/register.html',{"form":form,"title":"Register"})



def profile(request):
    profile = Profile.objects.get(user=request.user)
    form = ProjectForm()
    mainform = ProfileForm(instance=request.user.profile)
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            user = request.user
            title = form.cleaned_data['title']
            url = form.cleaned_data['url']
            location = form.cleaned_data['location']
            description = form.cleaned_data['description']
            image = form.cleaned_data['image']
            created_project = Project(title=title,url=url,location=location,description=description,image=image,user=user)
            created_project.save()
            return redirect('home')
    if request.method == 'POST':
        mainform = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if mainform.is_valid():
            mainform.save()
            return redirect('profile')
    return render(request, 'ip3/profile.html',{"title":"Profile","form":form,"mainform":mainform,"profile":profile})


#API endpoints
class ProfileViewApi(APIView):
    def get(self,request,*args,**kwargs):
        profiles = Profile.objects.all()
        serializer = ProfilesSerializer(profiles, many=True)
        return Response(serializer.data)
    

class ProjectViewApi(APIView):
    def get(self,request,*args,**kwargs):
        projects = Project.objects.all()
        serializer = ProjectsSerializer(projects, many=True)
        return Response(serializer.data)