from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, CreateTeamForm
from .models import Team, Comment, Task

def index(request):
	return HttpResponse("Welcome")

@login_required
def tasks(request):
	return HttpResponse("tasks")


@login_required
def teams(request):
	user = request.user
	return HttpResponse('teams')

def register(request):
	if(request.method == 'POST'):
		form = RegisterForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data['username']
			email = form.cleaned_data['email']
			password = form.cleaned_data['password1']
			firstname = form.cleaned_data['firstname']
			lastname = form.cleaned_data['lastname']
			user = User.objects.create_user(username = username, email = email, password = password)
			user.first_name = firstname
			user.last_name = lastname
			user.save()
			print('Registration Complete')
			return redirect('http://127.0.0.1:8000/accounts/login/')
		else:
			return render(request, 'register.html', {'form' : form})
	else:	
		form = RegisterForm()
		args = {'form': form}
		return render(request, 'register.html', args)

@login_required
def createTeam(request):
	if(request.method == 'POST'):
		form = CreateTeamForm(request.POST)
		if form.is_valid():
			teamName = form.cleaned_data['teamName']
			members = form.cleaned_data['members']
			members = members.split()
			team = Team.objects.create(name = teamName, creator = request.user)
			for member in members:
				user = User.objects.get(username = member)
				team.members.add(user)

			return render(request, 'createteam.html')
		else:
			return render(request, 'createteam.html', {'form' : form})
	else:
		form = CreateTeamForm()
		args = {'form' : form}
		return render(request, 'createteam.html', args)

@login_required
def teams(request):
	user = request.user
	queryset = user.team_set.all()
	print(queryset)
	for team in queryset:
		print(team)
	args = {'teams' : queryset}
	return HttpResponse('ok')