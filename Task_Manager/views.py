from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.http import HttpResponse, Http404
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, CreateTeamForm, CommentForm,  AddMemberForm, EditTaskForm, CreateTaskForm
from .models import Team, Comment, Task

# View Function for home
def home(request):
	return redirect('login')

# View Function to register
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
			return render(request, 'registeredUser.html')
		else:
			return render(request, 'registerUser.html', {'form' : form})
	else:	
		form = RegisterForm()
		args = {'form': form}
		return render(request, 'registerUser.html', args)

# View Function for Create Team
@login_required
def createTeam(request):
	if(request.method == 'POST'):
		form = CreateTeamForm(request.POST)
		if form.is_valid():
			teamName = form.cleaned_data['teamName']
			members = form.cleaned_data['members']
			description = form.cleaned_data['description']
			members = members.split()
			team = Team.objects.create(name = teamName, creator = request.user, description = description)
			for member in members:
				user = User.objects.get(username = member)
				team.members.add(user)

			return redirect('teams')
	else:
		form = CreateTeamForm()
	args = {'form' : form}
	return render(request, 'createTeam.html', args)



# View Function for create task
@login_required
def createTask(request, teamId):

	team = get_object_or_404(Team, pk=teamId)
	user = request.user
	if team.creator != user and user not in team.members.all():
		raise Http404("Unauthorized Access")

	if(request.method == 'POST'):
		form = CreateTaskForm(request.POST)
		if form.is_valid():
			title = form.cleaned_data['title']
			status = form.cleaned_data['status']
			description = form.cleaned_data['description']
			dueDate = form.cleaned_data['dueDate']
			members = form.cleaned_data['members']
			members = members.split()
			task = Task.objects.create(title= title, description = description, status= status, createdBy= user, dueDate= dueDate, team= team)
			task.assignedTo.add(user)
			for member in members:
				assignee = User.objects.get(username = member)
				if assignee in team.members.all():
					task.assignedTo.add(assignee)
			return redirect('tasks', team.pk)
	else:
		form = CreateTaskForm()
	args = {'team': team, 'form' : form}
	return render(request, 'createTask.html', args)

# View Function for list teams
@login_required
def teams(request):
	user = request.user
	queryset = user.team_set.all()
	queryset1 = Team.objects.filter(creator = user)   #teams created by user
	queryset2 = queryset.exclude(creator = user)  	#other teams

	args = {'teams1' : queryset1, 'teams2' : queryset2, 'user' : user}
	return render(request, 'teamsList.html', args)

# View Function for list tasks
@login_required
def tasks(request, teamId):
	user = request.user
	team = get_object_or_404(Team, pk = teamId)
	if request.user not in team.members.all() and request.user != team.creator:
		raise Http404("Unauthorized Access")

	tasks1 = Task.objects.filter(createdBy = user, team = team) #tasks created by user for team
	tasks2 = Task.objects.filter(assignedTo = user, team = team) #tasks assigned to user
	tasks2 = tasks2.exclude(id__in = tasks1)	
	tasks3 = team.task_set.exclude(id__in = tasks1) #all remaining tasks of team
	tasks3 = tasks3.exclude(id__in = tasks2)

	args = {'tasks1': tasks1, 'tasks2': tasks2, 'tasks3': tasks3, 'team': team, 'user' : user}
	return render(request, 'tasksList.html', args)

# View Function for task details
@login_required
def taskDescription(request, teamId, taskId):
	user = request.user
	form = CommentForm()
	args = {'form' : form}

	team = get_object_or_404(Team, pk = teamId)
	if request.user not in team.members.all() and request.user != team.creator:
		raise Http404("Unauthorized Access")
	task = get_object_or_404(Task, pk = taskId)
	comments = task.comment_set.all()
	if task.team != team:
		raise Http404("Team Mismatch")
	
	if request.method == 'POST':
		form = CommentForm(request.POST)
		if form.is_valid():
			body = form.cleaned_data['body']
			Comment.objects.create(body = body, author = user, task = task)
			args['msg'] = 'Comment Done'

		else:
			args['form'] = form

	args['task'] = task
	args['user'] = user
	args['team'] = team
	args['comments'] = comments
	args['assignedTo'] = task.assignedTo.all()

	return render(request, 'viewTask.html', args)

# View Function for edit team
@login_required
def editTeam(request, teamId):
	user = request.user
	team = get_object_or_404(Team, pk = teamId)
	if request.user != team.creator:
		raise Http404("Unauthorized Access")
	args = {'user': user, 'team':team, 'form':AddMemberForm()}
	
	if request.method == 'POST':
		if 'member' in request.POST:
			form = AddMemberForm(request.POST)
			if form.is_valid():
				user = User.objects.get(username= form.cleaned_data['member'])
				if user in team.members.all() or team.creator == user:
					args['msg'] = str(user.username) +' already in team.'
				else:
					team.members.add(user)
					args['msg'] = str(user.username) +' added to team.'	

			else:
				members = team.members.all()
				args['form'] = form
				args['members'] = members
		
		else:
			member = list(request.POST)[1]
			user = User.objects.get(username = member)
			team.members.remove(user)
			
	members = team.members.all()
	if len(members) == 0:
		args['msg'] = 'No members in team.'
	args['members'] = members
	return render(request, 'editTeam.html' ,args)

# View Function for team details
@login_required
def viewTeam(request, teamId):
	user = request.user
	team = get_object_or_404(Team, pk = teamId)
	if request.user not in team.members.all() and request.user != team.creator:
		raise Http404("Unauthorized Access")

	members = team.members.all()
	args = {'team': team, 'user': user, 'members':members}
	return render(request, 'viewTeam.html' ,args)

# View Function for edit task
@login_required
def editTask(request, teamId, taskId):
	team = get_object_or_404(Team, pk=teamId)
	task = get_object_or_404(Task, pk=taskId)
	user = request.user
	if task.team != team or task.createdBy != user:
		raise Http404("Unauthorized Access")
	form = EditTaskForm(instance= task)
	form2 = AddMemberForm()
	if request.method == "POST":
		if 'member' in request.POST:
			form2 = AddMemberForm(request.POST)
			if form2.is_valid():
				assignee = User.objects.get(username= form2.cleaned_data['member'])
				if assignee in task.assignedTo.all():
					msg = str(assignee.username) +' already assigned.'
				elif assignee not in team.members.all():
					msg = str(assignee.username) + ' not in team.'
				else:
					task.assignedTo.add(assignee)
					msg = str(assignee.username) +' assigned to task.'	
			else:
				members = team.members.all()

		elif 'title' in request.POST:
			form = EditTaskForm(request.POST, instance=task)
			if form.is_valid():
				task = form.save(commit=False)
				task.createdBy = user
				task.team = team
				task.save()
				msg = 'Changes Saved'
			form = EditTaskForm(instance=task)
		else:
			member = list(request.POST)[1]
			assignee = User.objects.get(username = member)
			task.assignedTo.remove(assignee)
			
	else:
		form = EditTaskForm(instance=task)
		form2 = AddMemberForm()
	assignedTo = task.assignedTo.all()
	args = {'team': team, 'user': user, 'form': form, 'form2': form2, 'assignedTo': assignedTo, 'task':task}
	return render(request, 'editTask.html', args)


