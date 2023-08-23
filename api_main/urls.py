from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path('new/', admin.site.urls)
]
