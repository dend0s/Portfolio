from django.shortcuts import render
from django.views.generic import ListView

from .models import Project


def index(request):
    return render(request, 'kirill/index.html')


def contact(request):
    return render(request, 'kirill/contact.html')


def resume(request):
    return render(request, 'kirill/resume.html')


class ProjectsList(ListView):
    model = Project
    template_name = 'kirill/projects.html'
    context_object_name = 'projects'
