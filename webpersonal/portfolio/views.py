from django.shortcuts import render
from .models import Project
# Create your views here.

def portafolio(requets):

    projects = Project.objects.all()
    return render(requets,"portfolio/portafolio.html", {'projects':projects})