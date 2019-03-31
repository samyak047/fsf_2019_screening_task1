
from django.test import TestCase
from django.urls import reverse
from django.test.client import Client
from django.contrib.auth.models import User
from . models import Team, Task, Comment

class ViewViewTests(TestCase):

	def test_default_index(self):
		'''
			test whether home page is rendered or not
		'''
		response = self.client.get(reverse('home'))
		self.assertEquals(response.status_code,302)

class ViewTests(TestCase):
	
	def setUp(self):
		'''
			Set Up for tests
		'''
		self.client = Client()
		self.user1 = User.objects.create_user('user1', 'user1@user1.com', 'password')
		self.user2 = User.objects.create_user('user2', 'user2@user2.com', 'password')
		self.user3 = User.objects.create_user('user3', 'user3@user3.com', 'password')
		
		
	
	def test_create_team(self):
		'''
			Test whether unauthorized user can create team or not
		'''
		response = self.client.get(reverse('createTeam'))
		self.assertEquals(response.status_code,302)
		self.client.login(username='user1', password='password')
		response = self.client.get(reverse('createTeam'))
		self.client.logout()
		self.assertEquals(response.status_code,200)

	def test_edit_team(self):
		'''
			Test whether only team creator can edit team or not
		'''

		#Unauthenticated user should be redirected to login
		team = Team.objects.create(name='Test', description='Test', creator= self.user1)
		response = self.client.get(reverse('editTeam', args=(team.pk,)))
		self.assertEquals(response.status_code,302)
		

		#Any user except creator should not edit team
		self.client.login(username='user2', password='password')
		response = self.client.get(reverse('editTeam', args=(team.pk,)))
		self.assertEquals(response.status_code, 404)
		self.client.logout()

		#Team creator should edit team
		self.client.login(username='user1', password='password')
		response = self.client.get(reverse('editTeam', args=(team.pk,)))
		self.assertEquals(response.status_code, 200)
		self.client.logout()


	def test_create_task(self):
		'''
			Only Team Members should be able to create task
		'''
		team = Team.objects.create(name='Test', description='Test', creator= self.user1)
		team.members.add(self.user2)

		self.client.login(username='user3', password='password')   #user not in team
		response = self.client.get(reverse('createTask', args=(team.pk,)))
		self.assertEquals(response.status_code,404)
		self.client.logout()

		self.client.login(username='user2', password='password')   #user is team member
		response = self.client.get(reverse('createTask', args=(team.pk,)))
		self.assertEquals(response.status_code,200)
		self.client.logout()

		
	def test_edit_task(self):
		'''
			Only Task creator can edit the task
		'''
		team = Team.objects.create(name='Test', description='Test', creator= self.user1)
		task = Task.objects.create(title='Testing',description='No desc',status='Pending',createdBy=self.user2,team=team)
		
		self.client.login(username='user1', password='password')
		response = self.client.get(reverse('editTask', args=(team.pk, task.pk,)))
		self.assertEquals(response.status_code, 404)
		self.client.logout()

		self.client.login(username='user2', password='password')
		response = self.client.get(reverse('editTask', args=(team.pk, task.pk,)))
		self.assertEquals(response.status_code, 200)
		self.client.logout()
		




		




		





