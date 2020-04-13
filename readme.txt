# mysite is the django project and projects is the django app

to run the project in the local server first you have to go activate the virtual environment by cd to the myenv folder 
and then hit the Scripts\activate command.
Then to actually run the server cd to C:\Users\user\Documents\Nouveau dossier\Udemy\django+PostgreSQL\myenv\mysite folder 
where the manage.py file is and hit python manage.py runserver



CREATE VIEWS		((((a view is basically like a web page inside your jungle application))))
to create view you should first go to views inside the application folder(projects) and write an httpresponse to get when access this view.
e.g from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
	return HttpResponse("Hello World")
Then create a urls.py inside the application folder(projects) to connect the view you just created with a url that accesses it.
e.g  from django.urls import path
from . import views

urlpatterns = [
	path('',views.index,name="index")
]
Lastly go to urls.py in project folder(mysite) and in list urlpatterns add a path to your application's urls.
e.g	path('projects/',include('projects.urls'))



CREATE MODELS


CREATE SUPERUSER ACCOUNT
python manage.py createsuperuser 	and fill username mail and password then go to your server(localhost:8000) /admin and you can log in




