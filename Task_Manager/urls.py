from django.urls import path
from . import views

urlpatterns = [

	path('', views.index, name='index'),
	path('tasks/', views.tasks, name='tasks'),
	path('teams/', views.teams, name='teams'),
	path('accounts/register/', views.register, name='register'),
	path('createteam/', views.createTeam, name='createTeam'),
	path('teams/', views.teams, name='teams')

]