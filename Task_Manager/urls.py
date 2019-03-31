from django.urls import path
from . import views

urlpatterns = [

	path('', views.home, name='home'),
	path('teams/', views.teams, name='teams'),
	path('register/', views.register, name='registerUser'),
	path('team/create/', views.createTeam, name='createTeam'),
	path('team/edit/<teamId>/', views.editTeam, name = 'editTeam'),
	path('team/view/<teamId>/', views.viewTeam, name = 'viewTeam'),
	path('task/create/<teamId>/', views.createTask, name = 'createTask'),
	path('team/tasks/<teamId>/', views.tasks, name='tasks'),
	path('task/view/<teamId>/<taskId>/', views.taskDescription, name='description'),
	path('task/edit/<teamId>/<taskId>/', views.editTask, name = 'editTask'),
	
	



]