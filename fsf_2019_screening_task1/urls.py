from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('Task_Manager.urls')),
    path('', include('django.contrib.auth.urls')),
]
