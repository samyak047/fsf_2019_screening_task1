from django.urls import path
from . import views

urlpatterns = [

	path('', views.home, name='home'),
	path('tasks/', views.tasks, name='tasks'),
	path('teams/', views.teams, name='teams'),
	path('accounts/register/', views.register, name='registerUser'),
	path('createteam/', views.createTeam, name='createTeam'),
	path('teams/', views.teams, name='teams'),
	path('tasks/<teamId>', views.tasks, name='tasks'),
	path('tasks/<teamId>/<taskId>', views.taskDescription, name='description'),

]