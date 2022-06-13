from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('project/<int:id>/', views.project, name='project'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('api/profiles/', views.ProfileViewApi.as_view(), name='profiles'),
    path('api/projects/', views.ProjectViewApi.as_view(), name='projects'),
]