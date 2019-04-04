from django.shortcuts import render,redirect
from django.http import HttpResponse, Http404,HttpResponseRedirect
import datetime as dt
from .models import Project ,User
from .forms import NewProjectsForm,ProfileForm
# from .email import send_welcome_email
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='/accounts/login/')
def projects_today(request):
    date = dt.date.today()
    all_projects = Project.objects.all()
    # projects= Projects.objects.all()
    print(all_projects)
    

    return render(request, 'today_projects.html', {"date": date, "projects":all_projects})




def search_results(request):

    if 'project' in request.GET and request.GET["project"]:
        search_term = request.GET.get("project")
        searched_images = Project.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"images": searched_images})

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
        return redirect('projectsToday')

    else:
        form = NewProjectsForm()
    return render(request, 'new_projects.html', {"form": form,"current_user":current_user,"title":title})
      
@login_required(login_url='/accounts/login/')
def myPicture(request,id):
    user = User.objects.get(id = id)
    # profiles = Profile.objects.get(user = user)
   
    return render(request,'profile.html',{"user":user})

@login_required(login_url='/accounts/login/')
def Profile(request):
    current_user = request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = current_user
            profile.save()

            return redirect('projectsToday')

    else:
        form = ProfileForm()
    return render(request, 'my_profile.html', {"form": form})