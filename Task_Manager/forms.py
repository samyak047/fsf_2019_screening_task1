from django import forms
from django.contrib.auth.models import User

class RegisterForm(forms.Form):
	firstname = forms.CharField(label = 'First Name')
	lastname = forms.CharField(label = 'Last Name')
	username = forms.CharField(label = 'Username')
	email = forms.EmailField(label = 'E-mail')
	password1 = forms.CharField(label = 'Password', widget=forms.PasswordInput())
	password2 = forms.CharField(label = 'Confirm Password', widget=forms.PasswordInput())
	
	def clean(self):
		cleaned_data = super().clean()
		p1 = cleaned_data.get("password1")
		p2 = cleaned_data.get("password2")
		username = cleaned_data.get("username")

		if len(User.objects.filter(username=username)) > 0:
			raise forms.ValidationError('Username already Exists')
		#if len(p1) < 8:
		#	raise forms.ValidationError('Password should be minimum 8 characters long.')
		if p1 != p2:
			raise forms.ValidationError('Both Password fields should be same.')
		

class CreateTeamForm(forms.Form):
	teamName = forms.CharField(label = 'Team Name')
	members = forms.CharField(label = 'Space separated username or email id of Members')

	def clean(self):
		cleaned_data = super().clean()
		members = cleaned_data.get("members")
		members = members.split()
		for member in members:
			if len(User.objects.filter(username = member)) == 0:
				raise forms.ValidationError('No user with username :'+member)
		

