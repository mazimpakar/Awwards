from django.shortcuts import render
from django.http  import HttpResponse
import datetime as dt
# Create your views here.

def welcome(request):
     return render(request, 'welcome.html')
def projects_of_day(request):
    date = dt.date.today()
    return render(request, 'today_projects.html', {"date": date,})