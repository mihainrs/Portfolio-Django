from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Project, AboutMe
from .forms import ProjectForm, AboutMeForm

#temp proj list (for testing purposes)
projects_list = [
   {'title': 'Project 1', 'description': 'Desc. for project 1', 'link': 'https://example.com/1'},
   {'title': 'Project 2', 'description': 'Desc. for project 2', 'link': 'https://example.com/2'},
   {'title': 'Project 3', 'description': 'Desc. for project 3', 'link': 'https://example.com/3'},
   {'title': 'Project 4', 'description': 'Desc. for project 4', 'link': 'https://example.com/4'},
]

#main/home view
def home(request):
    return render(request, 'projects/home.html')

#projects view
def projects(request):
    #getting all projects from db
    projects = Project.objects.all() 
    return render(request, 'projects/projects.html', {'projects' : projects})

#Django built-in SU view
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user) #to log them in automatically
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'projects/signup.html', { 'form':form})

#adding project
@login_required
def add_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('projects')
    else:
        form = ProjectForm()
    return render(request, 'projects/add_project.html', {'form':form})

#editing project
@login_required
def edit_project(request, pk):
    project = get_object_or_404(Project, pk=pk)
    form = ProjectForm(request.POST or None, instance=project)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('projects')
    else:
        form = ProjectForm(instance=project)
        
    return render(request, 'projects/edit_project.html', {'form':form})

#deleting project
@login_required
def delete_project(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.method == 'POST':
        project.delete()
        return redirect('projects')
    return render(request, 'projects/delete_confirm.html', {'project':project})

#about me section
def about_me(request):
    #first line of entry
    about_me = AboutMe.objects.first()
    if not about_me:
        #If no AboutMe instance exists, create a default one or handle the case
     return render(request, 'projects/about_me.html', {'about_me': None})
    return render(request, 'projects/about_me.html', {'about_me':about_me})

def edit_about_me(request,pk):
    #getting about me obj using the primary key
    about_me = get_object_or_404(AboutMe, pk=pk)
    
    if request.method == 'POST':
        form = AboutMeForm(request.POST, request.FILES, instance=about_me)
        if form.is_valid():
            form.save()
            return redirect('about_me')
    else:
        form=AboutMeForm(instance=about_me)
    return render(request, 'projects/edit_about_me.html',{'form':form})