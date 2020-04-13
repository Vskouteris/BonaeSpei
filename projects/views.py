from django.shortcuts import render
from django.http import HttpResponse
from .models import Project
# Create your views here.

def index(request):
	projects = Project.objects
	return render(request,'projects/index.html',{'projects':projects})
	
def iCage(request):
	projects = Project.objects
	return render(request,'projects/icage.html',{'projects':projects})