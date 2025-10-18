# core/views.py
from django.shortcuts import render
from .models import Skill

def home(request):
    skills = Skill.objects.all().order_by('category', 'display_order')
    return render(request, 'core/home.html', {'skills': skills})

def about(request):
    skills = Skill.objects.all().order_by('category', 'display_order')
    return render(request, 'core/about.html', {'skills': skills})

def contact(request):
    return render(request, 'core/contact.html')