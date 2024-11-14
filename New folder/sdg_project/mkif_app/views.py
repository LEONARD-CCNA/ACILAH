# mkif_app/views.py
from django.http import HttpResponse
from django.shortcuts import render
from .models import ResearchDocument, InnovationProject, Communication

def home(request):
    return render(request, 'mkif_app/home.html')

def research_list(request):
    documents = ResearchDocument.objects.all()
    return render(request, 'mkif_app/research_list.html', {'documents': documents})

def project_list(request):
    projects = InnovationProject.objects.all()
    return render(request, 'mkif_app/project_list.html', {'projects': projects})

def communication_list(request):
    communications = Communication.objects.all()
    return render(request, 'mkif_app/communication_list.html', {'communications': communications})
