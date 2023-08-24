
from django.contrib import admin
from django.urls import path, include

urlpartterns = [
    path('admin/',admin.site.urls),
    path('',include("projetApp.urls"))
]
