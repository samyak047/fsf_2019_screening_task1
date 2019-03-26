from django.contrib import admin
from .models import Task, Comment, Team

admin.site.register(Team)
admin.site.register(Task)
admin.site.register(Comment)