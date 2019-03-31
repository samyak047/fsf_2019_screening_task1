from django.db import models
from django.contrib.auth.models import User

class Team(models.Model):
	name = models.CharField(max_length = 100)
	description = models.CharField(max_length = 200)
	creator = models.ForeignKey(User, null=False, related_name="team_created_by", on_delete=models.CASCADE)
	
	members = models.ManyToManyField(User)
	createdAt = models.DateTimeField(auto_now_add=True)
	def __str__(self):
		return str(self.name)

	class Meta:
		ordering = ['-createdAt']

class Task(models.Model):
	title = models.CharField(max_length=200)
	description = models.TextField(null=True)
	status = models.CharField(max_length=100)
	
	createdBy = models.ForeignKey(User, null=False, related_name="task_created_by", on_delete=models.CASCADE)
	assignedTo = models.ManyToManyField(User, default=createdBy, related_name="task_assigned_to")
	
	createdAt = models.DateTimeField(auto_now_add=True)
	dueDate = models.DateField(blank=True, null=True)

	team = models.ForeignKey(Team, on_delete=models.CASCADE)		
	
	def __str__(self):
		return str(self.title)

	class Meta:
		ordering = ['-createdAt']

class Comment(models.Model):
	body = models.CharField(max_length=500)
	task = models.ForeignKey(Task, on_delete=models.CASCADE)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	createdAt = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return str(self.body)

	class Meta:
		ordering = ['createdAt']

