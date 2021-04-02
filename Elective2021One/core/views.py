from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required

from django.template import loader
from django.http import HttpResponse

from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.
def login(request):
	context = {}
	if request.method == "POST":
		username = request.POST.get('username')
		password = request.POST.get('password')

		user = auth.authenticate(username=username,password=password)

		if user is not None:
			auth.login(request,user)
			return redirect("/")
		else:
			context = {"message":"Invalid Login Credentials"}

	template = loader.get_template('login.html')
	return HttpResponse(template.render(context, request))

@login_required
def home(request):
	return render(request, 'home.html')

@login_required
def settings(request):
	return render(request,'settings.html')