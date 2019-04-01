from django.shortcuts import render,redirect
from django.http import HttpResponse, Http404,HttpResponseRedirect
import datetime as dt
from .models import Projects 
from .forms import NewProjectsForm
# from .email import send_welcome_email
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='/accounts/login/')
def projects_today(request):
    date = dt.date.today()
    all_projects = Projects.all_projects()
    projects= Projects.objects.all()
    print(projects)
    
#     if request.method == 'POST':
        
        
#         form = NewProjectsForm()
    return render(request, 'today_projects.html', {"date": date, "projects":all_projects})




def search_results(request):

    if 'projects' in request.GET and request.GET["projects"]:
        search_term = request.GET.get("projects")
        searched_projects = Projects.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"projects": searched_projects})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})

@login_required(login_url='/accounts/login/')
def projects(request,projects_id):
    try:
        project= Projects.objects.get(id = projects_id)
    except DoesNotExist:
        raise Http404()
    return render(request,"projects.html", {"projects":projects})

@login_required(login_url='/accounts/login/')
def new_projects(request):
    current_user = request.user
    title = 'New projects'
    if request.method == 'POST':
        form = NewProjectsForm(request.POST, request.FILES)
        if form.is_valid():
            projects = form.save(commit=False)
            projects.user = current_user
            projects.save()
        return redirect('todaysProjects')

    else:
        form = NewProjectsForm()
    return render(request, 'new_projects.html', {"form": form,"current_user":current_user,"title":title})